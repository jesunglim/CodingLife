import bitcoin.main as btc

passpharse = 'Brain Wallet 테스트 개인키'
privKey = btc.sha256(passpharse)
dPrivKey = btc.decode_privkey(privKey, 'hex')
if dPrivKey < btc.N:        # secp256k1의 N보다 작으면 ok
    # 개인키로 공개키를 생성한다
    pubkey = btc.privkey_to_pubkey(privKey)

    # 공개키로 지갑 주소를 생성한다 (mainnet용)
    address = btc.pubkey_to_address(pubkey, 0)

    # 결과 확인
    print("\n\nPasspharse :", passpharse)
    print("\n개인키 :", privKey)
    print("개인키 --> 공개키 :", pubkey)
    print("\n공개키 --> 지갑 주소 :", address)
else:
    print("요청하신 Passpharse로 개인키를 만들었으나, 유효하지 않습니다.")
    print("다른 Passphrase로 다시 시도해주세요")