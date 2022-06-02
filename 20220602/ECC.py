import math

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

a = 2
b = 2
p = 32416189381
G = (5,1)


d = 1234567 # private key

# Double-and-Add 알고리즘으로 공개키 생성
bits = bin(d)
bits = bits[2:len(bits)]

K = G

bits = bits[1:len(bits)]
for bit in bits:
    # Double
    K = addOperation(a, b, K, K, p)

    # Multiply
    if bit == '1':
        K = addOperation(a, b, K, G, p)
    
privKey = d
pubKey = K

print("\nDomain parameters : (P, a, b, G)")
print("P = %d" % p)
print("a = %d" % a)
print("b = %d" % b)
print("G = (%d, %d)" % (G[0], G[1]))
print("EC : y^2 = x^3 + %d * x + %d mod %d" % (a, b, p))
print("\nKeys :")
print("Private Key = ", privKey)
print("Public Key = %d * (%d, %d) = (%d, %d)" % (d, G[0], G[1], pubKey[0], pubKey[1]))
