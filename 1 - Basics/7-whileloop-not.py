# Describes usage of while (conditions) statement

# Can have multiple conditions using boolean operators
# Boolean operators are seperated with 'and' OR 'or' keys
# 'not' is also a boolean operator checking for
#       presence or absence of specific 
#       value/object based on python object specifications
# Following uses 'or' boolean operator as well
# Can have single or multiple conditions 
#       seperated by boolean operators

# USAGE
# while (condition):
#   execution block

name = ''
age = 0
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
