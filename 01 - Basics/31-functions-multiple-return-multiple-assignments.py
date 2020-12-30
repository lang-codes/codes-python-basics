# HEAD
# Python Functions - No Return, Single Return, Multiple returns
# DESCRIPTION
# Describes returning values from functions
#
# Can have Single return value from function
# 'return' value, when is a single return value
#       keeps the type in return statement
# Can return multiple values from a function
# 'return' values, when multiple return values,
#       gets coverted to the type of tuple
# Python has First-class functions - https://en.wikipedia.org/wiki/First-class_function
#           It treats functions as first-class citizens, means the language supports passing
#           functions as arguments to other functions, returning them as the
#           values from other functions, and assigning them to variables or
#           storing them in data structures.
# RESOURCES
#

# Return values can be captured in a variable
#       during invocation (Single or Multiple return values)
# Values can be destructured and assigned
#       to multiple variables (Multiple return values)
# The return values are of specific types as returned
#       and not a tuple in this case
# The number of items in the destructuring have to be
#       the same as variables used for assignation

# A function with no return value returns a None value
# A function with a return statement and no value in return
#       returns a None value
# A function can return one return value
# A function can return multiple return values - type will be tuple
# https://stackoverflow.com/questions/39345995/how-does-python-return-multiple-values-from-a-function
# A function can pack multiple return values into a
#       different type but construct them into a different type like list or diction or set


# Declaring a function with multiple return values
def helloMultiple(name):
    print('Howdy! ' + name)
    # Following two return statements are equal
    # Explicit
    # return ('name', name)
    # Implicit
    return 'name', name


# Capture multiple returns as a tuple in a variable
mul = helloMultiple('Testing Multiple returns')
print(mul)


# Capture multiple returns in different variables using destructuring
var1, var2 = helloMultiple(
    'Testing Multiple returns captured in multiple values')
print(var1, var2)


# Return tuple (default) with multiple items from function
def myfunReturnTupleImplicit():
    return 1, 2, 3
v1, v2, v3 = myfunReturnList()
print(v1, v2, v3)


# Return tuple with multiple items from function
def myfunReturnTupleExplicit():
    return (1, 2, 3)
v1, v2, v3 = myfunReturnList()
print(v1, v2, v3)


# Return set with multiple items from function
def myfunReturnSet():
    return {1, 2, 3}
v1, v2, v3 = myfunReturnList()
print(v1, v2, v3)


# Return dict with multiple items from function
def myfuncReturnDiction():
    return {0: 1, 1: 2, 2: 3}
v1, v2, v3 = myfunReturnList()
print(v1, v2, v3)


# Return list with multiple items from function
def myfunReturnList():
    return [1, 2, 3]
v1, v2, v3 = myfunReturnList()
print(v1, v2, v3)


# # # ERROR SCENARIOS DURING MULTIPLE ASSIGNATIONS

# # Return list with multiple items from function and 
# #       incorrect assignation leads to error
# def myfunReturnList():
#     return [1, 2, 3]
# v1, v2, v3, v4 = myfunReturnList()
# print(v1, v2, v3, v4)

# # Return list with multiple items from function and 
# #       incorrect assignation leads to error
# def myfunReturnList():
#     return [1, 2, 3]
# v1, v2 = myfunReturnList()
# print(v1, v2)


# Single line functions can also be defined
# It may act as a replacement for anonymous lamda functions
#       where you need named reference or 
#       reuse of function definitions and also return multiple returns
def func(x): return "some val", x
v1, v2 = func(1)
print(mul)

