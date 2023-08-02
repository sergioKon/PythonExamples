thistuple = ("apple", "banana", "cherry")
print(thistuple)
tup1=(10,20,30,40)
print(type(thistuple))

text = "GeeksforGeeks"
mySet = {text }

myDic = {}

count = myDic['a']
count+=1

for char in enumerate(text):
    if char in myDic:
       myDic[char]+=1
    else:
       myDic[char]=1

print(myDic)
