# HEAD
# Classes - as Objects with method access
# DESCRIPTION
# Describes 
#       - working of instantiator, 
#       - passing of values in constructor,
#       - using objects as classes
# RESOURCES
# 


# using classes as objects
class Foo:
    def __init__(self, val):
        self.val = val

obj1 = Foo(12)

# function definition
def printVal(self):
    print(self.val)

# Assigning function to class as an object
Foo.printVal = printVal
# Access obj1 methods, public attributes and properties
obj1.printVal()
