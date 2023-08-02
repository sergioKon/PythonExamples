class Base:
 
    # Declaring public method
    def fun(self):
        print("Public method")
 
    # Declaring private method
    def _fun(self):
        print("base protected  method")
 
# Creating a derived class
 
 
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
 
    def call_public(self):
 
        # Calling public method of base class
        print("\nInside derived class")
        self.fun()
    
    def _fun(self):
        print("derived protected  method")
 
    def call_private(self):
 
        # Calling private method of base class
        self._fun()
 
 
# Driver code
obj1 = Base()

# Calling public method
obj1.fun()
 
obj2 = Derived()
obj2.call_public()
obj2.call_private()

# Uncommenting obj1.__fun() will
# raise an AttributeError
 
# Uncommenting obj2.call_private()
# will also raise an AttributeError