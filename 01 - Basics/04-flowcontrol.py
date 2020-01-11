# Describes usage of if...elif...else statement

# 'if' key creates a set of conditional 
#       blocks of which one is triggered
# 'if' key needs a condition to be fulfilled
# Only 'if' statement needed
# 'elif' statement can be any number
# 'else' statement is not compulsary
# There can one 'if' & one 'else'
# Does not create a private/local scope of its own
# Takes or shares scope of the level it is defined in

# 'if' key has to have a condition that 
#       returns a Boolean value
# 'if' key can also be 
#       followed by a boolean directly
# A condition checks for equality of two values or variables
# 'else' does not have a condition 
#       and executes if any above 'if' or 'elif' 
#       statements fails

# USAGE
# if (conditions):
#   execution block
# elif conditions:
#   execution block
# else:
#   execution block

name = input()
password = input()
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    elif (password == 'alternate'):
        print('else if block alternate password')
    else:
        print('Wrong password.')


# SINGLE LINE FLOWCONTROL IF STATEMENT

# value_when_true if condition else value_when_false
# expression if (condition) else expression
name = "string"
print("it is a string") if (name == "string") else print("it is not a string")
