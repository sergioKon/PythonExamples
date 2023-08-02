import cProfile
from ctypes import *
'''def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
'''
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        if num > 10:
            break
def generator_function():
    for i in range(3):
        yield i


file="C:/kafka-1/config/zookeeper.properties"
#print(csv_reader(file))
'''
for i in infinite_sequence():
     print(i, end=" ")
     '''
'''
seq=infinite_sequence()
print(next(seq))
print(next(seq))
print(next(seq))
'''

i = c_int()

#cProfile.run('sum([i * 2 for i in range(10000)])')
#cProfile.main()
#gen = generator_function()
#print(next(gen))