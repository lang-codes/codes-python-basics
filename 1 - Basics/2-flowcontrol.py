# Describes usage of if...else statement
# input() is a inbuilt function that takes input from user in command line

# 'if' key creates a set of conditional 
#       blocks of which one is triggered
# 'if' key needs a condition to be fulfilled
# 'else' statement is not compulsary
# Only 'if' statement needed
# There can one 'if' and one 'else'
# 'if' creates a block
# Does not create a private/local scope of its own
# Takes or shares scope of the level it is defined in

# Creates a conditional block, however
#       Can have single or multiple conditions 
#       seperated by boolean operators

# USAGE
# if (condition):
#   execution block

# Round brackets are optional
# if condition:
#   execution block

# Can have single or multiple conditions
# if (condition) and (condition):
#   execution block

name = input()
password = input()
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
