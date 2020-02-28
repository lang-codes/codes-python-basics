# HEAD
# Classes - Public Access Modifiers
# DESCRIPTION
# Describes how to create public attributes and work with them
# Public 
# RESOURCES
# 


# Creating Parent class
class Parent():
    # Public Attributes
    par_cent = "parent"

    _par_cent = "protected"
    __par_cent = "private"

    # Parent Init method
    def __init__(self, val):
        self.par_cent = val
        print("Parent Instantiated")
    def method(self):
        print("Parent par_cent", self.par_cent)


# Creating ParentTwo class
class Child(Parent):

    # Child Init method
    def __init__(self, val_two):
        self.p = super()
        self.p.__init__(val_two)
        print("self.par_cent", self.par_cent)
    def child_method(self):
        print("Child par_cent", self.par_cent)
        self.method()
        print(self.p.method())


obj = Child(10)


# Public attributes/methods can be accessed on instance object
print("obj.par_cent", obj.par_cent)
obj.child_method()


# # Protected attributes/methods loggically should not be 
# #         accessed on instance object
# # ERROR
# # Traceback (most recent call last):
# #   File "19-classes-public-access-modifiers.py", line 37, in <module>
# #     print("obj._par_cent", obj._par_cent)
# # AttributeError: 'Child' object has no attribute '_par_cent'
# # 
# # BUGGY:
# # I have had Ubuntu Linux 
# #      throwing errors & working for same code.
# # Non-replicable
# print("obj._par_cent", obj._par_cent)


# # Private attributes/methods can be accessed on instance object
# # ERROR
# # Traceback (most recent call last):
# #   File "19-classes-public-access-modifiers.py", line 47, in <module>
# #     print("obj.__par_cent", obj.__par_cent)
# # AttributeError: 'Child' object has no attribute '__par_cent'
# print("obj.__par_cent", obj.__par_cent)

