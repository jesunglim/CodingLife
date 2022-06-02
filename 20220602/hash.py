from Crypto.Hash import SHA256

msg = '이 문서의 Hash value를 계산한다?'
print('\nMessage : ', msg)

msg = msg.encode()

# SHA256
h = SHA256.new()
h.update(msg)
hv = h.hexdigest()
print("    SHA256 (%d bit) : %s" % (len(hv) * 4, hv))


# Double-SHA256
h1 = SHA256.new()
h1.update(msg) # 1st SHA256

h2 = SHA256.new()
h2.update((h1.hexdigest()).encode()) # 2nd SHA256
hv = h2.hexdigest()
print("Double-SHA256 (%d bit) : %s" % (len(hv) * 4, hv))