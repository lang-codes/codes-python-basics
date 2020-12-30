# HEAD
# Python FlowControl - while loops
# DESCRIPTION
# Describes usage of while (and conditions) loop statements
#
# Since the condition is always true,
#       the loop below is infinite loop
#
# Declaring a 'while' loop with one condition
# The loop will keep iterating till the
#       value of name is not 'your name'. This may
#       become a infinite loop if the user does not
#       enter the value 'your name'
#
# Describes usage of while (conditions) statement
#       using `not` with conditions
#
# Can have single or multiple conditions
#       and uses boolean operators as conditions
#
# Conditions are seperated with Boolean operators 'and' OR 'or' keys
#
# 'not' is also a boolean operator checking for
#       presence or absence of specific
#       value/object/boolean based on python object
#       specifications. A value or object presence is denoted as Truthy
#
# Use with boolean operator - and, or, not
#           with any combination is possible
#
# RESOURCES
#


# USAGE:

# Defining a name with blank string
name = ''

# # Following loop is always infinite due to the condition
# while name != 'your name':
#     print('Enter your name.')
#     # Getting a new string value for name
#     name = input()
# print('Thank you!')


# while condition or condition:
#       execution block

# while (not condition or condition) and (condition):
#       execution block


# Defining name and age
name = ''
age = 0


# Defining a while loop with multiple conditions separated
#       with boolean operators
while (not name) or (not age) or (age == 0):
    if (name and age == 0):
        print('Please enter your age ')
        age = input()
    if (not name):
        print('Enter a new name')
        name = input()
    if (age):
        print('Hello ' + str(name) + ', your age is ' + str(age))
    else:
        print('Hello ' + str(name))
print('Finished loop')

