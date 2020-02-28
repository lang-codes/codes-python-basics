# HEAD
# Classes - Access Modifiers
# DESCRIPTION
# Describes how to create public, pritected, private attributes
# Public, Protected, Private
# RESOURCES
# 


# Creating Parent class
class Parent():
    # Public Attributes
    par_cent = "parent"

    # Protected Attributes
    _par_cent = "protected parent"

    # Private Attributes
    __par_cent = "private parent"

    # Parent Init method
    def __init__(self, val):
        self.par_cent = val
        print("Parent Instantiated with ", self.par_cent)


# Creating ParentTwo class
class Child(Parent):

    # Child Init method
    def __init__(self, val_two):
        self.p = super()
        self.p.__init__(val_two)

obj = Child(10)

# Public attributes/methods can be accessed on instance
print("obj.par_cent", obj.par_cent)
# Protected attributes/methods can be accessed on instance
print("obj._par_cent", obj._par_cent)

# # Private attributes/methods can be accessed on instance
# # Will error out
# print("obj.__par_cent", obj.__par_cent)
