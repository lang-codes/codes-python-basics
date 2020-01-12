# HEAD
# Python FlowControl - DecisionFlow using `not` with conditions
# DESCRIPTION
# Describes usage of while (conditions) statement 
#       using `not` with conditions
# 
# Can have single or multiple conditions 
#       and uses boolean operators as conditions
# Conditions are seperated with Boolean operators 'and' OR 'or' keys
# 'not' is also a boolean operator checking for
#       presence or absence of specific 
#       value/object based on python object specifications
# Use with boolean operator - and, or, not
#           with any combination
# RESOURCES
# 


# USAGE:

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
