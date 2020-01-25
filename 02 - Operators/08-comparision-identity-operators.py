# HEAD
# Comparision Indentity Operators
# DESCRIPTION
# Describes how comparision identity operators are used
# RESOURCES
# 

# Comparision Identity operators in a 
#       conditional expression checks for
#       two values OR variable+value OR
#       variable+variable
# Returns boolean value

# Operation, Meaning
# is - object identity
# is not - negated object identity

name = "test"

if (type(name) is str):
    print('is operator', name, 1)

# is operator checks if obj is of same type
if name is None:
    print('is operator', name, 4)

if name is name:
    print('is operator', name, 5)

if name is "test":
    print('is operator', name, 6)

# 'is not' operator checks inverse of 'is' operator
if name is not int:
    print('is not operator', name, 7)

# if name not == name (Error)
# if name != name (Works)
# if name is not name (Works)
# if not name == name (Works)
# if name (Works - name -> object)- 
#       [ 0, undefined var == False ]
#       [ -1, 1, defined var == True ]

