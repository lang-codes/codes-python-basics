# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes how inheritance works in classes in python
# RESOURCES
# 

# OVERRIDING (GOOD) AND POLYMORPHISM 
# https://www.geeksforgeeks.org/polymorphism-in-python/
# MULTIPLE INHERITANCE (GOOD) and POLYMORPHISM (GOOD)
# https://overiq.com/python-101/inheritance-and-polymorphism-in-python/

# Parent class with init and method
class Parent:
    def __init__(self, val):
        self.val = val
        
    def printVal(self):
        print(self.val)

# Simple inheritance of Parent class by DerivedChild
# DerivedChild class with a method and inheritance of Parent class
class DerivedChild(Parent):
    def negateVal(self):
        self.val = -self.val

class DerivedChildtwo(DerivedChild):
    def negateVal(self):
        self.val = -self.val

# Instantiate the child class - DerivedChild
obj1 = DerivedChild(12)
obj1.negateVal()
obj1.printVal()
obj1.negateVal()
obj1.printVal()

# isinstance is an instance of Foo class
print(isinstance(obj1, Parent))

# issubclass function below checks if DerivedFoo is an inherited class of Foo
print(issubclass(DerivedChildtwo, Parent))
