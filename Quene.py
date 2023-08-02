


class PriorityQueue:
    items=[]
    def __init__(self,top, items):
        self.top = top
        self.items = items

    def insert(self):
        ipos=0
        index =0 # in case items is empty and you need it after the loop
        stack=[];
        while(index<self.top):
         stack.append(-1)
         index+=1

        index=-1
        while (index < len(self.items)):
            # print(self.items[index])
             index+=1
             count=0
             while(count < self.top-1):
               if(self.items[index]> stack[count]):
                 stack[count]= stack[count+1]
                 count+=1
               else:
                break
             stack[count]= self.items[index]
        print(stack)
    

list = [0, 10, 30, 2, 7, 5, 90, 76, 100, 45, 55]   #-1 -1 -1 -1
pQuene = PriorityQueue(4,list)
pQuene.insert()
#print(list)