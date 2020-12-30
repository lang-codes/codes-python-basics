# HEAD
# Python Basics - String Data Types
# DESCRIPTION
# Describes how
#       - create and use single and multi-line strings
#       - using str function to convert to string
#       - using str function to convert python object to string
#       - fetch string representation for python objects
#
# RESOURCES
#


# ITERATORS
# Iterators are those objects that can be iterated or looped


# # SEQUENCE ITERATORS
# Sequence based Iterators allow identification or reference
#       of every loop-able item with an INDEX


# # # STRING

# Single line string
var = "String"


# Multi line string
var = """
Multi Line 
String
"""


# Multi line string created and ignored
"""
Multi Line 
String
"""


# Using str function to create a string
var = str("String")

var = str(1)

var = str("1")

var = str(True)

var = str(False)


# Using str function to create a string from function
def myfunc():
    pass


var = str(myfunc)


# Using str function to create a string from class
class MyClass:
    pass


var = str(MyClass)

