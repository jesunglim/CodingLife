import os
import math
import random
import time
import hashlib

# Additive Operation
def addOperation(a, b, p, q, m):
    if q == (math.inf, math.inf):
        return p

    x1 = p[0]
    y1 = p[1]
    x2 = p[0]
    y2 = p[1]

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

# CSPRNG 방식, os.urandom()과 random()을 적당히 섞어서 hash256dmfh
# 256비트 난수를 생성한다
def random_key():
    r = str(os.urandom(32)) \
        + str(random.randrange(2**256)) \
        + str(int(time.time() * 1000000))
    r = bytes(r, 'utf-8')
    h = hashlib.sha256(r).digest()
    key = ''.join('{:02x}'.format(y) for y in h)
    return key

# secp256k1의 Domain parameters
# y^2 = x^3 + 7 mode m
a = 0
b = 7
m = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
G = (0x79BE667EF9DCBBAC55A06295CE870B070B07029BFCDE28D959F2815B16F81798,
     0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# 개인키를 생성한다.
while(1):
    d = int(random_key(), 16)
    if d > 0 & d < n:
        break

# Dobuble-and-Add 알고리즘으로 공개키를 생성한다
bits = bin(d)
bits = bits[2:len(bits)]

# initialize. bits[0] = 1 (always)
K = G

# 두 번째 비트부터 DObule-and-Add 알고리즘을 적용한다
bits= bits[1:len(bits)]
for bit in bits:
    # Double
    K = addOperation(a, b, K, K, m)

    # Multiply
    if bit == '1':
        K = addOperation(a, b, K, G, m)
    
privKey = d
pubKey = K
print("\nPrivate Key : ", hex(privKey))
print("\n Public Key : (%s, \n          %s)" % (hex(pubKey[0]), hex(pubKey[1])))