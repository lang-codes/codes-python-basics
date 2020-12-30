# HEAD
# Python Basics - Data Types List
# DESCRIPTION
# Describes different data types available in Python
#       Python is Object Oriented Language that supports
#               Object Oriented Programming
#
# RESOURCES
#

# Everything in Python is an Object
# Following are some Data Type Objects in Python

# CORE PYTHON DATA TYPES
# # NoneType
# # Boolean
# # Integer
# # Float
# ITERATORS
# # SEQUENCE ITERATORS
# # # String
# # # List
# # # Tuple
# # NON-SEQUENCE ITERATORS
# # # Dictionary
# # # Sets
# # # Frozen Sets
# # Function
# # Elipses
# # Classes
# # Methods
# # Modules
# # Custom Types
# LIBRARY or MODULE BASED DATA TYPES/STRUCTURES
# # Array
# # Date, Calender, etc


# CORE PYTHON DATA TYPES

# # NONETYPE (NoneType)
# None Type is an Object

var = None

# # BOOLEAN
# Boolean Type is an Object
var = True
var = False

# Following behave as BOOLEAN
var = 0  # Falsy
var = 1  # Truthy
var = var  # Truthy since it is an object

# # INTEGER
var = 1

# # FLOAT
var = 1.2

# ITERATORS
# Iterators are those objects that can be iterated or looped

# # SEQUENCE ITERATORS
# Sequence based Iterators allow identification or reference
#       of every loop-able item with an INDEX

# # # STRING
var = "String"

var = """
Multi Line 
String
"""

# # # LIST
# Integer based list
var = [1, 2, 3]

# String Type List (can also be any other type based list)
var = ["s", "t", "r", "i", "n", "g"]

# Mixed Type List
var = [1, 1.2, "s", True, None, False, [1, "s"], (1, "s"), {"s": 20}]

# # # TUPLE
# Integer Type Tuple (can also be any other type based Tuple)
var = (1,)

# Integer Type Tuple (can also be any other type based Tuple)
var = (1, 2)

# String Type Tuple (can also be any other type based Tuple)
var = ("s", "t", "r", "i", "n", "g")

# Mixed Type Tuple
var = (1, "s")

# Mixed Type Tuple
var = (1, 1.2, "s", True, None, False, [1, "s"], (1, "s"), {"s": 20})

# # NON-SEQUENCE ITERATORS
# Sequence based Iterators allow identification or reference
#       of every loop-able item with an KEY or NO REFERENCE/KEY/INDEX

# # # DICTIONARY
# Dictionaries are key value pairs with key as a reference for item value
# Dictionaries can have integer or string as key
# Value can be of any type

# Dictionary cn have integer as key
var = {1: "s"}

# Dictionary can have string as key
var = {"name": []}

# # # SETS
# Sets are like lists with no reference of item like Index or Key
# Sets look like lists but with a round bracket in definitions
# Sets can only have unique items

# Sets with mixed value
var = {1, "s"}

# # # FROZEN SETS
# Frozen sets are sets which are immutable

var = frozenset({1, "s"})

# # FUNCTION

vara = lambda x:x

def varb(x): return x

# # ELIPSES


# # CLASSES

class varc():
    pass

# # METHODS

class vard():
    def method(self):
        pass

# # MODULES
# Every folder or file behaves like a module in Python

# LIBRARY or MODULE BASED DATA TYPES/STRUCTURES

# # ARRAY

from array import array
var = array('i', [1, 2, 3])

# # DATE, CALENDER, etc

from datetime import date
var = date.today()

from calendar import Calendar
var = Calendar().iterweekdays()

# # CUSTOM TYPES

class MyOwnTypeImplementation():
    pass

# # DATA STRUCTURES

# 5.1.1. Using Lists as Stacks
# 5.1.2. Using Lists as Queues
# 5.1.3. List Comprehensions
# 5.1.4. Nested List Comprehensions


