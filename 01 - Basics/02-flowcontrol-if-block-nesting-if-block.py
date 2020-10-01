# HEAD
# Python FlowControl - Decision flow - if block
# DESCRIPTION
# Describes the decision making flow control usage
# 
# 'if' key creates a set of conditional 
#       blocks of which one is triggered
# 'if' key needs a condition to be fulfilled
# 'else' statement is not compulsary
# Only 'if' statement is compulsory and needed
# There can one 'if' and one 'else'
# 'if' creates a block
# Does not create a private/local scope of its own
# Takes or shares scope of the level it is defined in
# 'if'...'else' can be nested
# RESOURCES
# 


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

# Take input of name
name = input("Enter name")

# Take input of password
password = input("Enter password")

# Initiating a block of if set of statements
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
