# HEAD
# Classes Introduction
# DESCRIPTION
# Describes how to create a blank block and a simple class
#       Use classes to create objects
# RESOURCES
# 

# # STRUCTURE
# class ClassName():
#     executionblock
# obj = ClassName()


# Creating a blank block with pass
class BlankBlock():
    pass

obj = BlankBlock()

# Creating a custom class
# Class name - MyCustomClass


class MyCustomClass():
    # class attribute
    attribute = "value"
    # class method
    def method(self):
        return "Testing method"


# Creating a class instance object
obj = MyCustomClass()

# Accessing a object attribute & methods
print("Access obj.attribute", obj.attribute)

# Accessing a object methods using invocation
print("Access obj.method()", obj.method())
