
def readMap(**kwargs):
    print (kwargs.keys())
    print (kwargs.items())

def readArgs( *args,name):
    print(name)
    for item in enumerate(args, start=0):
    #for i in range(len(args)):

        print(item)

def readParams(id, year, model="Fiat"):
    print('{} {} {}'.format(id,model, year))

def generator_function():
    for i in range(10):
        yield i

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})

#readMap(key=car)
#parse=readArgs
readParams(year=2016,id=10)
#generator_function()
#parse( "first","second", "third","forth","fifth",name="data")
print("name = ", __name__)