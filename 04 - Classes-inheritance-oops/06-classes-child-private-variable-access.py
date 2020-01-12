# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes how parent and child access works in inheritance
# RESOURCES
# 


# Privacy is just a notion and denoted as following:
# __attribute refers to the fact that attribute is private
# The double '__' refers that it is private
# '__method__(self)' refers to the fact that method is private
# All private references donot stop us from accessing 
#       the private attriutes, properties, and methods

# Private variables
# https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes

# parent class with printVal function and init
class Parent:
    def __init__(self, val):
        self.__val = val
    def printVal(self):
        print(self.__val)

# overrides printVal of Parent into its own implementation
class DerivedChild(Parent):
    def supersVal(self):
        print('My value is %s' % self.__val)

obj1 = DerivedChild(12)
obj1.printVal()
obj1.supersVal()

# Traceback (most recent call last):
#   File "70-classes-private-variable-access.py", line 15, in <module>
#     obj1.supersVal()
#   File "70-classes-private-variable-access.py", line 11, in supersVal
#     print('My value is %s' % self.__val)
# AttributeError: 'DerivedChild' object has no attribute '_DerivedChild__val'
