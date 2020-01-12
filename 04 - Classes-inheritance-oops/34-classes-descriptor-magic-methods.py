# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes the magic methods of classes
# RESOURCES
# 
# https://rszalski.github.io/magicmethods/

# Building Descriptor Objects

# Descriptors are classes which, when accessed through either getting, setting, or deleting, can also alter other objects. Descriptors aren't meant to stand alone; rather, they're meant to be held by an owner class. Descriptors can be useful when building object-oriented databases or classes that have attributes whose values are dependent on each other. Descriptors are particularly useful when representing attributes in several different units of measurement or representing computed attributes (like distance from the origin in a class to represent a point on a grid).

# To be a descriptor, a class must have at least one of __get__, __set__, and __delete__ implemented. Let's take a look at those magic methods:

# __get__(self, instance, owner)
#     Define behavior for when the descriptor's value is retrieved. instance is the instance of the owner object. owner is the owner class itself.
# __set__(self, instance, value)
#     Define behavior for when the descriptor's value is changed. instance is the instance of the owner class and value is the value to set the descriptor to.
# __delete__(self, instance)
#     Define behavior for when the descriptor's value is deleted. instance is the instance of the owner object.

# Now, an example of a useful application of descriptors: unit conversions.

# class Meter(object):
#     '''Descriptor for a meter.'''

#     def __init__(self, value=0.0):
#         self.value = float(value)
#     def __get__(self, instance, owner):
#         return self.value
#     def __set__(self, instance, value):
#         self.value = float(value)

# class Foot(object):
#     '''Descriptor for a foot.'''

#     def __get__(self, instance, owner):
#         return instance.meter * 3.2808
#     def __set__(self, instance, value):
#         instance.meter = float(value) / 3.2808

# class Distance(object):
#     '''Class to represent distance holding two descriptors for feet and
#     meters.'''
#     meter = Meter()
#     foot = Foot()
