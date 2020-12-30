# HEAD
# Python Basics - Creating variables
# DESCRIPTION
# Describes how to create/define variables
#   
# 
# RESOURCES
# 

# STRUCTURE
# variable_target_name | equal_to_assignment_operator | target_value
#       definition = declaration and assignment
var = 10

# VALUE POSSIBILITIES
# You can assign any type of values/objects to a variable

# # BARE BASIC TYPES
#   - Python is a Object Oriented Language (Everything is an object in Python)
#       - None (representing a null value is also an object)
#       - Boolean Values (True / False)
#       - Integer Values - Number Value Type with no decimals (1, 2, ...)
#       - Float Values - Decimal Value Types (1.0, 1.2, 1.20, 1.21, 1.234...)
#       - String Values ("string")
#       - Multi-Line String Values ("""string""")
#       - List Values ([1,2,"b", "c"])
#       - Tuple Values ((1,2,"b", "c"))
#       - Objects (Any object, list, tuple, array, function, etc. All above types are objects)

# None # (representing a null value is also an object)
var = None

# Boolean Values (True / False)
var = True
var = False

# Integer Values - Number Value Type with no decimals (1, 2, ...)
var = 10

# Float Values - Decimal Value Types (1.0, 1.2, 1.20, 1.21, 1.234...)
var = 10.2

# String Values ("string")
var = "Single line string"

# Multi-Line String Values ("""string""")
var = """
Multi
Line
String
"""

# List Values ([1,2,"b", "c"])
#   Can take any data type as an item
var = [1, 1.1, "string", """Multiline string""", [], (), {}, None, True]

# Tuple Values ((1,2,"b", "c"))
#   Can take any data type as an item
#   Tuple is same as list but immutable
var = [1, 1.1, "string", """Multiline string""", [], (), {}, None, True]

# Objects 
#   Any object, list, tuple, array, function, etc. 
#   All above types are objects
class TestObject():
    pass
var = TestObject

