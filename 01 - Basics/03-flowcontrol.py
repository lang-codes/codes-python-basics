# HEAD
# Python FlowControl - Decision flow
# DESCRIPTION
# Describes usage of if...elif statements 
#       without need of else statement
# 
# 'if' key creates a set of conditional 
#       blocks of which one is triggered
# 'if' key needs a condition to be fulfilled
# Only 'if' statement needed
# 'elif' statement can be any number
# Can have any number of 'elif' statements
# Does not create a private/local scope of its own
# Takes or shares scope of the level it is defined in
# RESOURCES
# 


name = 'Dracula'
age = 4000

# Initiating a block of if...elif...else set of statements
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
