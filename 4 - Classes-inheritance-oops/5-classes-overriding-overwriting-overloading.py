# Describes overiding, overwriting, and overloading concepts

# OVERWRITING
# def funct():
#     pass

# def funct():
#     print('val')

# OVERLOADING - Theoritically not possible in python classes
# Using different forms of function execution implementation
# https://overiq.com/python-101/operator-overloading-in-python/
# Due to absence of types
# def getInt(val):
#     print(val)
# def getInt(str(val), someotherval):
#     print(val)

# OVERRIDING
# parent class with printVal function
class Foo:
    def __init__(self, val):
        self.val = val
    def printVal(self):
        print(self.val)

# overrides printVal of Foo into its own implementation
class DerivedFoo2(Foo):
    def printVal(self):
        print('My value is %s' % self.val)

obj1 = DerivedFoo2(12)
obj1.printVal()