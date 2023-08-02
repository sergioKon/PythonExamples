import hashlib
password = "hahaha"

myHashObject = hashlib.sha256(password.encode())
print(" my hash = ",myHashObject.hexdigest())

text = 'Hello!'

m = hashlib.sha256(text.encode('UTF-8'))


outHash= '28ea98b16640fa7c1716164e3a3b034c77ba909ce13fa65dd08f026fcd3a63b2'
for i in range(1,10000):
    fullPassword= (password + str(i)).encode()
    hexDigest=hashlib.sha256(fullPassword).hexdigest()
    if hexDigest == outHash:
        print(i, password+ str(i))
        break
