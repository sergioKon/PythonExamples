import hashlib

sourceHash =  'a5122d74dcc64664028eeca11bd84c50'

for userId in  range(1000):
    for password in range(1000):
            data= str(555^userId)+ str(password)
            dataBytes = data.encode()
            destHash = hashlib.md5(dataBytes).hexdigest()
            if(destHash == sourceHash):
                print(' user = {} password = {} '.format(userId, password) )
                exit()



