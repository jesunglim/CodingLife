import math
import random
from Crypto.Hash import SHA256

# secp256k1의 Domain parameters
# y^2 = x^3 + 7 mod m
a = 0
b = 7
m = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
G = (0x79BE667EF9DCBBAC55A06295CE870B070B07029BFCDE28D959F2815B16F81798,
     0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


# Addition Operation
def addOperation(a, b, p, q, m):
    if q == (math.inf, math.inf):
        return p

    x1 = p[0]
    y1 = p[1]
    x2 = q[0]
    y2 = q[1]

    if p == q:
        r = 2 * y1
        rInv = pow(r, m-2, m)
        s = (rInv * (3 * (x1 ** 2) + a)) % m
    else:
        r = x2 - x1
        rInv = pow(r, m-2, m)
        s = (rInv * (y2 - y1)) % m
    x3 = (s ** 2 - x1 - x2) % m
    y3 = (s * (x1 - x3) - y1) % m
    return x3, y3

# 개인키 생성
def generatePrivKey():
    while(1):
        d = random.getrandbits(256)
        if d > 0 & d < n:
            break
    return d

# 공개키 생성
def generatePubKey(d, g):
    bits = bin(d)
    bits = bits[2:len(bits)]

    # initialize bits[0] = 1 (always)
    K = g

    bits = bits[1:len(bits)]
    for bit in bits:
        K = addOperation(a, b, K, K, m)

        if bit == '1':
            K = addOperation(a, b, K, g, m)
    return K

# 서명할 문서
message = '이 문서를 서명합니다'
message = message.encode()

# 서명자의 개인키와 공개키를 생성한다
d = generatePrivKey()
Q = generatePubKey(d, G)

# ephemeral 키 생성
k = generatePrivKey()
x, y = generatePubKey(k, G)
r = x % n

# Singing
h = SHA256.new()
h.update(message)
hx = h.hexdigest()
hx = int(hx, 16)


invK = pow(k, n-2, n)
s = ((hx + d * r) * invK) % n


# 전자서명을 보낸다
print("\nMessage =", message.decode())
print("\n전자서명 생성 :")
print("h(x) =", hex(hx))
print("   r =", hex(r))
print("   s =", hex(s))
#==================================

# Verification
w = pow(s, n-2, n)
u1 = (w * hx) % n
u2 = (w * r) % n
v1 = generatePubKey(u1, G)
v2 = generatePubKey(u2, Q)
x, y = addOperation(a, b, v1, v2, m)

print("\n전자서명 확인 :")
print("h(x) =", hex(hx))
print("   x =", hex(x))
print("   r =", hex(r))


if r == x % n:
    print("\n* Valid Signature")
else:
    print("\n* Invalid Signature")