import fibo
def output( text, array, number):
     print(text[:2]+"\t"+text[len(text) * -1 :  ]  + ' language ')    
     array.append(number*number)
     print(array)

def concat(*args,sep="/"):
    return sep.join(args)

print("Hello world")
print(concat("earth", "mars", "venus"))
text = "Python"
squares= [1,4,9,16,25]
output(text, squares, 6)
fibo.fib(5)