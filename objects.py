class SwappableTuple:
    def __init__(self, srcTupl):
        self.srcTupl = srcTupl
    
    def swap(self):
        swapped = self.srcTupl[::-1]
        self.srcTupl=swapped
        return self.srcTupl

srcTupple= (1,2,3,4)
swapTupple = SwappableTuple (srcTupple)       
t= swapTupple.swap()
print (t)
x= swapTupple.swap()
print(x)
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
index=int(letters.__len__()/2)

print(letters[index])
