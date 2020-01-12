# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes usage of 
#       metaclass for creating classes instead of 
#       default type class
# Type to create class
# RESOURCES
# 



# 3.3.3.1. Metaclasses
# https://docs.python.org/3/reference/datamodel.html#metaclasses
# The potential uses for metaclasses are boundless. 
# Some ideas that have been explored include 
# enum, logging, interface checking, automatic delegation, 
# automatic property creation, proxies, frameworks, 
# and automatic resource locking/synchronization.
# Look at documentation

# Sample codes
# https://gist.github.com/pjeby/75ca26f8d2a7a0c68e30

# Describes Meta and __call__ magic methods
# https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python

# CREATING CLASS DIRECTLY USING TYPE
# >>> MyClass = type('MyClass', (), {})
# >>> MyClass
# <class '__main__.MyClass'>

# Creating a empty metaclass that extends type
class Meta(type):
    pass

# Adding the metaclass with Meta class
class MyClass(metaclass=Meta):
    def test(self):
        print("My test")

# Extending the MyClass for MySubClass
class MySubclass(MyClass):
    def tester(self):
        print("My tester")

# Instantiating the class MySubclass
obj = MySubclass()
obj.

