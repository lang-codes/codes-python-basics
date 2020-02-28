# HEAD
# Classes - Object Lifecycle
# DESCRIPTION
# Describes how classes and object lifecycle work
# Public 
# RESOURCES
# 

# Creating Parent class
class Parent():
    par_cent = "Attribute"
    
    # Parent New method is also there but 
    #       runs before the object has been created and 
    #       the args are 
    #       __new__(cls, name, bases, dct)
    #       Next runs the Init method

    # Parent Init method
    def __init__(self, val):
        self.__par_cent = val
        print("Parent Instantiated")

    # Parent Call method
    def __call__(self, val):
        self.__par_cent = val
        print("__call__ invoked self.__par_cent", self.__par_cent)

    # Parent Delete method
    def __del__(self):
        print("__del__ invoked self.__par_cent", self.__par_cent)


# Invokes the __init__ method
obj = Parent(10)
print("Printing obj", obj)

# Invokes the __call__ method
obj(20) 

# Invokes the __del__ method
del obj

# # Traceback (most recent call last):
# #   File "22-classes-object-lifecycle.py", line 39, in <module>
# #     print("Printing obj", obj)
# # NameError: name 'obj' is not defined
# print("Printing obj", obj)

