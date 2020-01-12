# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes the magic methods of classes
# RESOURCES
# 
# https://rszalski.github.io/magicmethods/

# Reflection

# You can also control how reflection using the built in functions isinstance() and issubclass()behaves by defining magic methods. The magic methods are:

# __instancecheck__(self, instance)
#     Checks if an instance is an instance of the class you defined (e.g. isinstance(instance, class).
# __subclasscheck__(self, subclass)
#     Checks if a class subclasses the class you defined (e.g. issubclass(subclass, class)).

# The use case for these magic methods might seem small, and that may very well be true. I won't spend too much more time on reflection magic methods because they aren't very important, but they reflect something important about object-oriented programming in Python and Python in general: there is almost always an easy way to do something, even if it's rarely necessary. These magic methods might not seem useful, but if you ever need them you'll be glad that they're there (and that you read this guide!).
