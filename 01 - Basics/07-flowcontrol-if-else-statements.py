# HEAD
# Python FlowControl - Decision flow - if-else block
# DESCRIPTION
# Describes the decision making flow control usage
#   Uses if...else or if...elif...else block for decision control
#
# 'if' keyword creates a set of conditional
#       blocks of which one is triggered
# 'if' keyword needs a condition to be fulfilled
# 'else' keyword statement is optional
# 'else' keyword statement has to be at the end of the if...else block
# Only 'if' keyword statement is compulsory and needed
# There can be only one 'if' and one 'else'
# 'if' keyword creates a block
# Does not create a private/local scope of its own
# Takes or shares scope of the level it is defined in
# 'if'...'else' keyword can be nested
# 
# RESOURCES
# 


# Creates a conditional block, however
#       Can have single or multiple conditions
#       seperated by boolean operators

# USAGE
# if (condition):
#   execution block
# else:
#   execution block

# Round brackets are optional
# if condition:
#   execution block
# else:
#   execution block

# Can have single or multiple conditions
# if (condition) and (condition):
#   execution block
# else:
#   execution block

# If keyword block is compulsory and else is optional
# if condition:
#   execution block


# Take input of name
name = input()

# Take input of password
password = input()

# Initiating a block of if set of statements
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
else:
    print('Else statement')


# Initiating a block with if statements and multiple conditions
#   'or' boolean operator condition
if name == 'Mary' or password == 'swordfish':
    print('Access granted.')
else:
    print('Else statement')


# Initiating a block with if statements and multiple conditions
#   'and' boolean operator condition
if name == 'Mary' and password == 'swordfish':
    print('Access granted.')
else:
    print('Else statement')


# Initiating a block with if statements and multiple conditions
#   'and' and 'not' boolean operator inside condition
if name == 'Mary' and not (password == 'swordfish'):
    print('Access granted.')
else:
    print('Else statement')


# Initiating a block with if statements and multiple conditions
#   'not' boolean operator inside condition
if not name == 'Mary':
    print('Access granted.')
else:
    print('Else statement')


# Initiating a block with if statements and multiple conditions
#   'not' boolean operator inside condition equivalent to !=
if name != 'Mary':
    print('Access granted.')
else:
    print('Else statement')


# Initiating a block with if statements with no else statement
if name == 'Mary' or password == 'swordfish':
    print('Access granted.')


# Initiating a block of if statement with no elif, else
# elif and else is optional
if name == 'Alice':
    print('Hi, Alice.')
# Below if is a different 'if' set of block
if name == 'Licy':
    print('Hi, Licy.')
