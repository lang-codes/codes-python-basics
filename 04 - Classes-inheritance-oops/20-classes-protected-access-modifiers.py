# HEAD
# Classes - Protected Access Modifiers
# DESCRIPTION
# Describes how to create protected attribute and work with them
# Public 
# RESOURCES
# 


# Creating Parent class
class Parent():
    # Protected Attributes
    _par_cent = "pProtected"
    
    par_cent = "pPublic"
    __par_cent = "pPrivate"

    # Parent Init method
    def __init__(self, val):
        self._par_cent = val
        print("Parent Instantiated")
    def method(self):
        print("Parent _par_cent", self._par_cent)


# Creating ParentTwo class
class Child(Parent):

    # Child Init method
    def __init__(self, val_two):
        self.p = super()
        self.p.__init__(val_two)
        print("self._par_cent", self._par_cent)
    def child_method(self):
        print("Child _par_cent", self._par_cent)
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

