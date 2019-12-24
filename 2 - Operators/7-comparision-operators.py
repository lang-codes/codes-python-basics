# Describes how comparision operators are used

# Comparision operators in a conditional expression checks for
#       two values OR
#       variable+value OR
#       variable+variable
# Returns 'boolean' value

# 'isinstance()' is an inbuilt function that checks
#       if a object is an instance of specific type

# Operation, Meaning

# < - strictly less than
# <= - less than or equal
# > - strictly greater than
# >= - greater than or equal
# == - equal to
# != not equal
# not - inverse of boolean (not a comparision but boolean operator)

# Basic class defintion to demostrate usage of operators


class nam:
    name = 1


name = "test"
tester = nam()

# Different usage of comparision operators
#       (in combination with boolean operators)

# if (not name == "test"):
# if not (name == "test"):
# if not type(name) == "str":
# if (name != "test"):

# Usage of == operator
if (type(name) == 'str'):
    print(name, 1)

# Usage of != (not equal to) operator
if (type(name) != str):
    print(name, 2)

# Usage of > (greater than) operator
if (2 > 3):
    print('(2 > 3)', (2 > 3), 3)

# Usage of < (lesser than) operator
if (2 < 3):
    print('(2 < 3)', (2 < 3), 4)

# Usage of >= (greater than equal to) operator
if (3 >= 4):
    print('(3 >= 4)', (3 >= 4), 5)

# Usage of <= (less than equal to) operator
if (3 <= 4):
    print('(3 <= 4)', (3 <= 4), 6)

# Usage of isinstance() function returns boolean
if (isinstance(name, str)):
    print('isinstance(name, str)', isinstance(name, str), 7)

# Usage of isinstance() function returns boolean
if (isinstance(tester, nam)):
    print('isinstance(tester, nam)', isinstance(tester, nam), repr(nam), 8)

# Usage of comparision & boolean operators together
if ((isinstance(name, str) == True) or (not name == 'test')):
    print(
        '((isinstance(name, str) == True) or (not name == "test"))',
        ((isinstance(name, str) == True) or (not name == 'test')),
        9
        )

# Usage of comparision & boolean operators together
if ((isinstance(name, str) == True) and not (name == 'test')):
    print(
        '((isinstance(name, str) == True) and not (name == "test"))',
        ((isinstance(name, str) == True) and not (name == 'test')),
        10
        )
