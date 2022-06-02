from random import Random
from Crypto.Cipher import AES
from Crypto import Random
import numpy as np

secretKey128 = b'0123456701234567'
secretKey192 = b'012345670123456701234567'
secretKey256 = b'01234567012345670123456701234567'

# 128bit key를 사용한다
secretKey = secretKey128
plainText = 'This is Plain text. It will be encrypted using AES with CBC mode'
print('\n\n')
print('원문 :')
print(plainText)

# CBC 모드에서는 plaint text가 128-bit(16Byte)의 배수가 돼야 하므로 padding이 필요함
# padding으로 NULL 문자를 삽입함. 수신잔즌 별도로 padding을 제거할 필요는 없음
n = len(plainText)
if (n % 16) != 0:
    n = n + 16 - (n % 6)
    plainText = plainText.ljust(n, '\0')

# initialization vector iv도 수신자에게 보내야 한다
iv = Random.new().read(AES.block_size)
ivcopy = np.copy(iv)
