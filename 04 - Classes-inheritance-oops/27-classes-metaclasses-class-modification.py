# HEAD
# Classes - Metaclasses for class modification
# DESCRIPTION
# Describes how to use metaclasses dynamically to modify classes during instatiation
# Describes how to add attributes to a metaclass 
#       or re-implement the type __call__ methods
# Public 
# RESOURCES
# 


# /opt/pycharm/pycharm-community-2019.2.1/bin# sh pycharm.sh
# Concept taken from following
# https://github.com/django/django/blob/master/django/db/models/base.py

# Creating a Base meta class using type
class ModelBase(type):
    # Creating a method to be applied to all classed extending metaclass ModelBase
    def hello(cls):
        print("Test", type(cls))
    # __new__ , __init__ , __call__ , __dict__
    # Overriding implementation of __init__ of type and returning a class
    def __init__(cls, name, bases, dct):
        # Printing arguments
        print('bases', bases)
        print('name', name)
        print('dict', dct)
        print('cls.__dict__', cls.__dict__)
        # Returning the class as is - No changes
        # init passes an argument of cls or self
        return super(ModelBase, cls).__init__(cls)

    def __call__(self, *args, **kwargs):
        # Adding hello and sayHello method
        setattr(self, "hello", self.hello)
        setattr(self, "sayHello", self.hello)
        # Returning the modified class with two new methods
        # Call does not pass a argument
        return super(ModelBase, self).__call__()

class MyTest(metaclass=ModelBase):
        attributesname = 10
        # Creating a method testhello
        def testhello(self):
            self.sayHello()
            print("Printing class details inside of MyTest", type(self))

# Instantiating MyTest class extended using the metaclass ModelBase
obj = MyTest()
# Checking availability of attributes/methods
obj.sayHello()
obj.hello()
obj.testhello()

