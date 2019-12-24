# Describes how to create a blank block and a simple class

# Class is created with a class key and name of the class
# USAGE
# class NameOfClass:
#       attributes/properties
#       methods(self):
#           execution block

# 'pass' creates an empty block
# All attributes, properties, and methods in python are empty
# __init__ is the constructor method for a class
# init is triggered when the class instanciates
# All methods including init takes self as the first argument

class BlankClass:
    # Pass statement creates an empty class
    pass

# Simple class with an attribute and simple method
class SimpleClass:
    val = "All atrributes, properties, and methods in python are public"
    def printVal(self):
        print(self.val)

# Simple class with a __init__ constructor
class SimpleClassWithInit:
    def __init__(self, val):
        self.val = val
    def printVal(self):
        print(self.val)
