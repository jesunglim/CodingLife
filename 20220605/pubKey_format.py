privKey = '0xd303429bf9580b23d5f22903dabcba81be83b2d78b9fbc0f4883d8fb29c77a22'

pubKey = ('0x659766217bc372ba788587939cab5995675831bf70c8a172db5a8e2c02', 
          '0x61abc9b5be6dcef7857b3d45d2cb6a00ee9f07d1f37ccc33f2b301e197')

# secp256k1에 정의된 domain parameter p 
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

# 공개키를 Uncompressed format으로 표시한다
uPubKey = '04' + pubKey[0] + pubKey[1]

# 공개키를 Compressed format으로 표시한다.
if int(pubKey[1], 16) % 2 == 0:
    cPubKey = '02' + pubKey[0]
else:
    cPubKey = '03' + pubKey[0]


# Compressed Format을 원래의 (x, y) Format으로 변환한다.
# p % 4 = 3 mod 4이므로 아래 공식을 적용 할 수 있음.
x = int(cPubKey[2:], 16)
a = (pow(x, 3, p) + 7) % p  # y^2
y = pow(a, (p+1)//4, p)     # y

prefix = int(cPubKey[:2], 16)
if(prefix == 2 and y & 1) or (prefix == 3 and not y & 1):
    y = (-y) % p

# 공개키 출력
print("\n Public Key : (%s,\n           %s)" % (pubKey[0], pubKey[1]))

# Uncompressed format 출력
print("\nUncompressed (size = %d):\n%s" % (len(uPubKey)*4, uPubKey))

# Compressed format 출력
print("\ncompressed (size = %d):\n%s" % (len(cPubKey)*4, cPubKey))


print("\nCompressed format --> Public Key :")
print("\n Public Key : (%s,\n           %s)" % (hex(x)[2:], hex(y)[2:]))