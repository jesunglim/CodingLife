import hashlib
import binascii

privKey = '884a54b077ea3469e088f4ca8a634e734de8aa0519555e38687763e09afaaa9b'

# Base58 Encoding
s = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

# version prefix를 추가한다. 0x80 ~ Private key WIF
# 공개키를 compressed form으로 사용할 때는 이 뒤에 '01'을 추가로 붙인다.
prefixPayload = '80' + privKey

# Chcksum을 구한다. version + payload에 double-SHA256을 수행하고
# 앞 부분의 4바이트를 prefixPayload 뒤에 추가한다
versionPayload = binascii.unhexlify(prefixPayload)
h = hashlib.sha256(hashlib.sha256(versionPayload).digest()).digest()
h = ''.join('{:02x}'.format(y) for y in h)
versionPayloadChecksum = prefixPayload + h[0:8]

# Base58Check encoding을 수행한다
eKey = int(versionPayloadChecksum, 16)
base58 = ''
while(1):
    m, r = divmod(eKey, 58)
    base58 += s[r]
    if m == 0:
        break
    eKey = m

wif = base58[::-1]
print("\n개인키 (Hex): ", privKey.lower())
print("개인키 (WIF): ", wif)