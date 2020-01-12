# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes how to add attributes to a metaclass or re-implement the type methods/properties
# RESOURCES
# 


# Concept taken from following
# https://github.com/django/django/blob/master/django/db/models/base.py
# Some code taken from a blog and a stackoverflow question. Untracked

# Creating a metaclass extending type
class UpperAttrMetaclass(type):
    # Defining a public and a private attribute to be added to all classes
    someValue = "My public someValue attribute from Custom meta UpperAttrMetaclass"
    __privateValue = "My private attribute from Custom meta UpperAttrMetaclass"

    # Defining custom method to be added to all classes
    def common_attribute_def(cls):
        print("Printing from a UpperAttrMetaclass.common_attribute_def to be added", cls.__hash__(cls))

    # Defining custom method to be added to all classes
    def second_attribute_def(cls):
        print("Printing from a UpperAttrMetaclass.second_attribute_def to be added", cls.__hash__(cls))

    # Defining __init__ method behaviour
    # Adding a method in the implementation to the class object
    # Implementation gets passed with clsname, bases, dct automatically
    # Implementation different from default
    def __init__(cls, clsname, bases, dct):
        print("Printing clsname, bases, dct from UpperAttrMetaclass:__init__", clsname, bases, dct)
        print("Initialising my init from UpperAttrMetaclass:__init__", cls.__hash__(cls))
        setattr(cls, 'common_attribute_def', cls.common_attribute_def)
        # init passes an argument of cls/self. Fails with clsname, bases, dct args
        return super(UpperAttrMetaclass, cls).__init__(cls)

    # Defining __call__ method behaviour
    # Adding a method and two attributes in the implementation to the class object
    def __call__(cls, *args, **kwargs):
        print('args, kwargs from UpperAttrMetaclass.__call__', args, kwargs)
        setattr(cls, "second_attribute_def", cls.second_attribute_def)
        setattr(cls, "someValue", cls.someValue)
        setattr(cls, "__privateValue", cls.__privateValue)
        print('__dict__ from UpperAttrMetaclass:__int__', cls.__dict__)
        # Call does not pass a argument
        return super(UpperAttrMetaclass, cls).__call__()

    # Defining a __new__ implementation behaviour for the metaclass
    # Converting all the attributes defined in the class to uppercase
    # Converts only attributes and methods to uppercase defined inside the class extending the metaclass
    # Try adding the common_attribute_def and see the behaviour - does not get added
    # Implementation gets passed with clsname, bases, dct automatically
    # Implementation different from default
    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        print('Printing clsname, bases, dct from type base class: UpperAttrMetaclass:__new__', clsname, bases, dct)
        # Convert attributes to uppercase (basically the dict keys)
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        # Try adding attrs/method like this and see behaviour
        # setattr(cls, 'common_attribute_def', cls.common_attribute_def)
    
        # __new__ passes arguments of cls/self, clsname, bases, dict
        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

# Creating base class for a sample bases in meta class defs
class BaseClassTwo:
    # Defining a mybasetwo method
    def mybasetwo(self):
        print("Extended: In mybasetwo function from BaseClassTwo")

# Creating base class for a sample bases in meta class defs
class BaseClass:
    # Defining a mybase method
    def mybase(self):
        print("Extended: In mybase function from BaseClass")

# Creating MyNewsClass extending two base classes and using a meta class defined above
class MyNewsClass(BaseClass, BaseClassTwo, metaclass = UpperAttrMetaclass):
    # Defining the __init__ method
    def __int__(self):
        super()

    # defining a method MyNewClassDef
    def MyNewClassDef(self):
        print("Usage: small caps attributes due to metaclass new_fn from MyNewsClass")

# Instantiation of class using the metaclass UpperAttrMetaclass which extends two base classes
obj = MyNewsClass()

# Checks for availability of methods
obj.MYNEWCLASSDEF()
obj.mybase()
obj.mybasetwo()
obj.common_attribute_def()
obj.second_attribute_def()
# Checks for availability of properties
print(obj.someValue)
print(obj.__privateValue)
# ?
print(obj.__dict__)
