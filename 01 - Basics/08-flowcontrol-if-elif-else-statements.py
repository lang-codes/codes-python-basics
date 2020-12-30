# HEAD
# Python FlowControl - Decision flow - if...elif blocks
# DESCRIPTION
# Describes usage of if...elif statements 
#       without need of else statement
# 
# 'if' keyword creates a set of conditional
#       blocks of which one is triggered
# 'if' keyword needs a condition to be fulfilled
# Only 'if' keyword statement is compulsory and needed
# There can be only one 'if' and one 'else'
# 'if' keyword creates a block
# Does not create a private/local scope of its own
# Takes or shares scope of the level it is defined in
# 'if'...elif...'else' keyword can be nested
# Can have any number of 'elif' keyword statements
# 'elif' has a condition like 'if' keyword
# You can have elif after if statement
# elif keyword statement is optional
# You can use any number of elif keyword conditions after if statement
# 'else' keyword statement is optional
# 'else' keyword statement has to be at the end of the if...elif...else block
# Does not create a private/local scope of its own
# Takes or shares scope of the level it is defined in
# 
# RESOURCES
# 


name = 'Dracula'
age = 4000

# Initiating a block of if...elif...else keyword set of statements
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('First Line elif')
elif age > 100:
    print('Second Line elif')
else:
    print('Else statement')


# Initiating a block of if...elif set of statements
if name == 'Alice':
    print('Hi, Alice.')
# else is optional
elif age < 12:
    print('First Line elif')
elif age > 100:
    print('Second Line elif')


# Initiating a block of if...elif set of statements
if name == 'Alice':
    print('Hi, Alice.')
# elif can have multiple conditions using boolean operators
elif age < 12 and age > 100:
    print('First Line elif')


# Initiating a block of if statement with no elif, else
if name == 'Alice':
    print('Hi, Alice.')
# elif and else is optional

