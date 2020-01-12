# HEAD
# Classes - Multiple Inheritence Classes usage
# DESCRIPTION
# Describes multiple inheritance of class from multiple classes
# RESOURCES
# 

# Declaration of first parent
class Parent:
    # Will not be accessible in the child class
    __test = None
    def __init__(self, val):
        self.val = val
    def printValFoo(self):
        print(self.val)
    # Will not be accessible in the child class
    def __printValFoo__(self):
        print(self.val)

# Declaration of second parent
class ParentTwo:
    def __init__(self, val):
        self.val = val
    def printValFoos(self):
        print(self.val)

# Simple inheritance of Foo class by DerivedChild
class DerivedChild(Parent, ParentTwo):
    def negateVal(self):
        self.val = -self.val

# Instatiating class and accessing methods
obj1 = DerivedChild('test')
obj1.printValFoo()
obj1.printValFoos()