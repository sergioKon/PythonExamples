import os
import base64

n=27       #1010 1001 1000 0111    
bi = bin(n)
print(bi.count("1") , bi)

n=33
bynary= bin(n)
size = len(bynary) -2
move = 0 
count=0
for move  in range(size):
    lastBit =(  n & (2 ** move) ) >> move
    if (lastBit == 1 ):
        count +=1 

print (" count = ", count)        
print (" bynary  = ", bynary )      
print( ( n & 1 ) >>0) 
print( ( n & 2 ) >>1 )
print( ( n & 4) >> 2 )
print(( 2 & 8) >> 3 ) 
     
exit()

num= list(str(123321))
size= len(num)
print(num)
isTrue=True
midIndex= int(size/2)
print(num[midIndex:])
print(num[0:midIndex])

for i in range(int(size/2)):
    if(num[i]== num[size-i-1]):
        continue
    else:
        isTrue=False
        break 
print(isTrue)        
exit()
 
message = "Python is fun"
message_bytes = message.encode('UTF-8')
base64_bytes = base64.b64encode(message_bytes)  
base64_message = base64_bytes.decode('ascii')

print(base64_message)


exit()

# Get the list of all files and directories
path = "C:/CPrograms/bigIndian/bigIndian/bigIndian/Debug"
dir_list = os.listdir(path)
paramsencoded = base64.encode('123','UTF-8')

print(paramsencoded)

''' 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)
for file in dir_list:
    dest=file+'calcs'
    reader = open(file, "r")
    writer= open(dest,"w")
    with open(dest, 'rb') as binary_file:
        binary_file_data = reader.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')
        writer.write(base64_encoded_data)
'''