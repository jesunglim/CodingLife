import os
import random
import time
import hashlib

# secp256k1의 Domain parameter(order of G)
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


# CSPRNG 방식, os.urandom()와 random()을 적당히 섞어서 hash256으로 256비트 난수 생성
def random_key():
    r = str(os.urandom(32)) \
        + str(random.randrange(2*256)) \
        + str(int(time.time() * 1000000))
    r = bytes(r, 'utf-8')
    h = hashlib.sha256(r).digest()
    key = ''.join('{:02x}'.format(y) for y in h)
    return key

# secp256k1의 n값보다 값으면 된다.
while(1):
    privKey = random_key()
    if int(privKey, 16) < N:
        break

print("PrivKey (Hex) : ", privKey)
print("PrivKey (Dec) : ", int(privKey, 16))