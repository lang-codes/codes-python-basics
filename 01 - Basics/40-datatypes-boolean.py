# HEAD
# Python Basics - Boolean Data Type
# DESCRIPTION
# Describes
#       - creating and using a boolean
#       - type conversion of python objects and numerics to boolean
#       - using booleans and python objects in conditional checks
#
# RESOURCES
#


# # BOOLEAN
# Boolean Type is an Object
var = True
var = False


# Following behaves as BOOLEAN
var = 0  # Falsy
var = 1  # Truthy
var = var  # Truthy since it is an object


# Creating a BOOLEAN using Python bool function
var = bool(1)
var = bool(0)
var = bool(True)


# Using any variable to create a boolean
var = 2000
var = bool(var)


# Using Boolean as result of condition
if True:
    print("True: Boolean")


# Using Integer Falsy value as result of condition
if 0:
    print("0: Boolean")


# Using Object for Truthy / Falsy Value as result of condition
if var:
    print("Var: Boolean")


# Using Condition to get a boolean
if var == True:
    print("Condition: Boolean")
