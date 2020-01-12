# HEAD
# Classes Abstract Classes
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

# 'is not' operator checks inverse of 'is' operator
if name is not int:
    print('is not operator', name, 4)
