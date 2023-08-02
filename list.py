myList=[1,2,3]
for idx, item in enumerate(myList):
    myList[idx] =item*10
    
list2= myList.reverse()
print(myList) 
list2= myList[:]
list2.append(150)
myList=[100,200,300]
list2.extend(myList)
print(list2[-1])
list3=['a','b']
list5=[1,2,3, ['a','b']]
import sys
print(list5[3][0], sys.version)

print('999999999999999999999999999999')
companies = ['Microsoft', 'Google', 'Apple']
if (n := len(companies)) == 1 and (first_company := companies[0]):
    print(f'We have only one company: {first_company}')
elif (n := len(companies)) > 1 and (first_company := companies[0]):
    print(f'We have such companies as: {", ".join(companies)}')
else:
    print(f'We have no companies')
exit()


myList.insert(0,myList[0]*10)
