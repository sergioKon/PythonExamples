
sum=0

f= open("C:/Python-Programs/data/file.txt","r")
while line:=f.readline():
      sum+= int(line)
print(sum)




exit()


with open('C:/Python-Programs/data/file.txt') as f:
     for i in f:
         sum += int(i)
     print(sum)

'''
for i in range(1,1):
    for j in range(1,2):
        print(" user_"+str(i)+"_"+ str(j)) 
print ("**********")        
'''