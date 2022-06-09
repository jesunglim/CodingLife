import bitcoin.main as btc

# 개인키 생성
while (1):
    privKey = btc.random_key()
    dPrivKey = btc.decode_privkey(privKey, 'hex')
    if dPrivKey < btc.N:
        break;

# 개인키로 공개키를 생성한다.
pubKey = btc.privkey_to_pubkey(privKey)

# 공개키로 지갑 주소를 생성한다. (mainnet 용)
address1 = btc.pubkey_to_address(pubKey, 0)

# 공개키로 160-bit public key hash를 생성한다
pubHash160 = btc.hash160(btc.encode_pubkey(pubKey, 'bin'))

# 160-bit public key hash로 지갑 주소를 생성한다. (위의 adress와 동일하다)
address2 = btc.hex_to_b58check(pubHash160, 0)

# 지갑 주소를 160-bit public key hash로 변환한다. (위의 pubHash160과 동일하다)
pubHash1601 = btc.b58check_to_hex(address2)

# 공개키로 testnet용 지갑 주소를 생성한다
adress3 = btc.pubkey_to_address(pubKey, 0x6f)

# 결과 확인
print("\n\n개인키 : ", privKey)
print("개인키 --> 공개키 : ", pubKey)
print("\n공개키 --> 지갑 주소 (1, mainnet 용) : ", address1)
print("공개키 --> 공개키 해시 : ", pubHash160)
print("\n공개키 해시 --> 지갑 주소 (2. mainnet 용) : ", address2)
print("지갑 주소 --> 공개키 해시 : ", pubHash1601)
print("지갑 주소 (Testnet 용) :", adress3)