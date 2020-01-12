# HEAD
# Classes - Magic Methods - Controlling Attribute Access
# DESCRIPTION
# Describes the magic methods of classes
#       getattr, getattribute, setattribute, delattr
# RESOURCES
# 
# https://rszalski.github.io/magicmethods/

# Controlling Attribute Access

# Many people coming to Python from other languages 
#       complain that it lacks true encapsulation 
#       for classes; that is, there's no way to 
#       define private attributes with public getter 
#       and setters. This couldn't be farther than 
#       the truth: it just happens that Python 
#       accomplishes a great deal of encapsulation 
#       through "magic", instead of explicit modifiers 
#       for methods or fields. 
# Take a look:

# __getattr__(self, name)
#     You can define behavior for when a user attempts to access an attribute that doesn't exist (either at all or yet). This can be useful for catching and redirecting common misspellings, giving warnings about using deprecated attributes (you can still choose to compute and return that attribute, if you wish), or deftly handing an AttributeError. It only gets called when a nonexistent attribute is accessed, however, so it isn't a true encapsulation solution.
# __setattr__(self, name, value)
#     Unlike __getattr__, __setattr__ is an encapsulation solution. It allows you to define behavior for assignment to an attribute regardless of whether or not that attribute exists, meaning you can define custom rules for any changes in the values of attributes. However, you have to be careful with how you use __setattr__, as the example at the end of the list will show.
# __delattr__(self, name)
#     This is the exact same as __setattr__, but for deleting attributes instead of setting them. The same precautions need to be taken as with __setattr__ as well in order to prevent infinite recursion (calling del self.name in the implementation of __delattr__ would cause infinite recursion).
# __getattribute__(self, name)
#     After all this, __getattribute__ fits in pretty well with its companions __setattr__ and __delattr__. However, I don't recommend you use it. __getattribute__ can only be used with new-style classes (all classes are new-style in the newest versions of Python, and in older versions you can make a class new-style by subclassing object. It allows you to define rules for whenever an attribute's value is accessed. It suffers from some similar infinite recursion problems as its partners-in-crime (this time you call the base class's __getattribute__ method to prevent this). It also mainly obviates the need for __getattr__, which, when __getattribute__ is implemented, only gets called if it is called explicitly or an AttributeError is raised. This method can be used (after all, it's your choice), but I don't recommend it because it has a small use case (it's far more rare that we need special behavior to retrieve a value than to assign to it) and because it can be really difficult to implement bug-free.

# You can easily cause a problem in your definitions 
#       of any of the methods controlling attribute 
#       access. Consider this example:

# def __setattr__(self, name, value):
#     self.name = value
#     # since every time an attribute is assigned, __setattr__() is called, this
#     # is recursion.
#     # so this really means self.__setattr__('name', value). Since the method
#     # keeps calling itself, the recursion goes on forever causing a crash

# def __setattr__(self, name, value):
#     self.__dict__[name] = value # assigning to the dict of names in the class
#     # define custom behavior here

# Again, Python's magic methods are incredibly 
#       powerful, and with great power comes great 
#       responsibility. It's important to know the 
#       proper way to use magic methods so you don't 
#       break any code.

# So, what have we learned about custom attribute access 
#       in Python? It's not to be used lightly. In 
#       fact, it tends to be excessively powerful and 
#       counter-intuitive. But the reason why it exists 
#       is to scratch a certain itch: Python doesn't seek 
#       to make bad things impossible, but just to make 
#       them difficult. Freedom is paramount, so you can 
#       really do whatever you want. Here's an example of 
#       some of the special attribute access methods in 
#       action (note that we use super because not all 
#       classes have an attribute __dict__):

# class AccessCounter(object):
#     '''A class that contains a value and implements an access counter.
#     The counter increments each time the value is changed.'''

#     def __init__(self, val):
#         super(AccessCounter, self).__setattr__('counter', 0)
#         super(AccessCounter, self).__setattr__('value', val)

#     def __setattr__(self, name, value):
#         if name == 'value':
#             super(AccessCounter, self).__setattr__('counter', self.counter + 1)
#         # Make this unconditional.
#         # If you want to prevent other attributes to be set, raise AttributeError(name)
#         super(AccessCounter, self).__setattr__(name, value)

#     def __delattr__(self, name):
#         if name == 'value':
#             super(AccessCounter, self).__setattr__('counter', self.counter + 1)
#         super(AccessCounter, self).__delattr__(name)
