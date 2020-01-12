# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes how to add attributes to a metaclass or re-implement the type __call__ methods
# RESOURCES
# 

# Concept taken from following
# https://github.com/django/django/blob/master/django/db/models/base.py

class ModelBase(type):
    # Attribute to be added
    def hello(cls):
        print("Test from hello", type(cls))

    # Redefining __init__
    def __init__(cls, name, bases, dct):
        print('bases from __init__', bases)
        print('name from __init__', name)
        print('dict from __init__', dct)
        print('cls.__dict__ from __init__', cls.__dict__)
        return super(ModelBase, cls).__init__(cls)

    # Redefining __call__
    # Creating a new object instance
    # Adding attrs
    def __call__(self, *args, **kwargs):
        mydict = {'sayHello': self.hello}
        print('args, kwargs from __call__', args, kwargs)
        for a in args:
            print('arg from __call__', a)
            mydict[a] = a
        # Call type method to create a class
        # This class is going to be a new object
        cls = type('ModelBase', (), mydict)
        setattr(cls, "hello", self.hello)
        return cls

class MyTest(metaclass=ModelBase):
        # Using a blank class since we are creating
        # an common attr from __call__ and not __new__
        pass

        # Creating a method testhello
        # def testhello(self):
        #     self.sayHello()
obj = MyTest()
obj.sayHello()
# This will get overridden since we are creating a new object inside __call__ of metaclass
# obj.testhello()
