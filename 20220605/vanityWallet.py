import bitcoin.main as btc

bFound = False
for i in range(30000):
    # 개인키를 생성한다
    while(1):
        privKey = btc.random_key()
        dPrivKey = btc.decode_privkey(privKey, 'hex')
        if dPrivKey < btc.N:
            break

    # 개인키로 공개키를 생성한다.
    pubKey = btc.privkey_to_pubkey(privKey)

    # 공개키로 지갑 주소를 생성한다. (mainnet용)
    address = btc.pubkey_to_address(pubKey, 0)

    # 지갑 주소 앞부분이 문자열인지 확인한다
    if address[1:4] == 'ABC':
        bFound = True
        break

if bFound:
    # 결과 확인
    print("\n\n개인키 : ",privKey)
    print("\n개인키 --> 공개키 : ", pubKey)
    print("\n공개키 --> 지갑 주소 : ", address)
else:
    print("찾지 못했습니다. 다시 시도해 주세요")