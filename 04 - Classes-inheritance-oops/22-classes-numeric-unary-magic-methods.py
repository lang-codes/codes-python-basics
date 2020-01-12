# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes the magic methods of classes
# RESOURCES
# 
# https://rszalski.github.io/magicmethods/


# Now would be a good time to note that you don't have to define 
#       every comparison magic method to get rich comparisons. 
#       The standard library has kindly provided us with a class 
#       decorator in the module functools that will define all 
#       rich comparison methods if you only define __eq__ 
#       and one other (e.g. __gt__, __lt__, etc.) 
#       This feature is only available in Python 2.7, but when 
#       you get a chance it saves a great deal of time and effort. 
#       You can use it by placing @total_ordering above your class definition.

# NUMERIC MAGIC METHODS

# Just like you can create ways for instances of your class to be compared with comparison operators, you can define behavior for numeric operators. Buckle your seat belts, folks...there's a lot of these. For organization's sake, I've split the numeric magic methods into 5 categories: unary operators, normal arithmetic operators, reflected arithmetic operators (more on this later), augmented assignment, and type conversions.
# Unary operators and functions

# UNARY OPERATORS and functions only have one operand, e.g. negation, absolute value, etc.

# __pos__(self)
#     Implements behavior for unary positive (e.g. +some_object)
# __neg__(self)
#     Implements behavior for negation (e.g. -some_object)
# __abs__(self)
#     Implements behavior for the built in abs() function.
# __invert__(self)
#     Implements behavior for inversion using the ~ operator. For an explanation on what this does, see the Wikipedia article on bitwise operations.
# __round__(self, n)
#     Implements behavior for the built in round() function. n is the number of decimal places to round to.
# __floor__(self)
#     Implements behavior for math.floor(), i.e., rounding down to the nearest integer.
# __ceil__(self)
#     Implements behavior for math.ceil(), i.e., rounding up to the nearest integer.
# __trunc__(self)
#     Implements behavior for math.trunc(), i.e., truncating to an integral.


class Unary(str):
    def __pos__(self):
        # Implements behavior for unary positive (e.g. +some_object)
    def __neg__(self):
        # Implements behavior for negation (e.g. -some_object)
    def __abs__(self):
        # Implements behavior for the built in abs() function.
    def __invert__(self):
        # Implements behavior for inversion using the ~ operator. For an explanation on what this does, see the Wikipedia article on bitwise operations.
    def __round__(self, n):
        # Implements behavior for the built in round() function. n is the number of decimal places to round to.
    def __floor__(self):
        # Implements behavior for math.floor(), i.e., rounding down to the nearest integer.
    def __ceil__(self):
        # Implements behavior for math.ceil(), i.e., rounding up to the nearest integer.
    def __trunc__(self):
        # Implements behavior for math.trunc(), i.e., truncating to an integral.

u = Unary(" Tes ")

