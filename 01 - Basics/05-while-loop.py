# HEAD
# Python FlowControl - while loops
# DESCRIPTION
# Describes usage of while (conditions) statement
# 
# The condition is checked everytime before 
#       iteration execution block starts
# 'while' loop creates a conditional block
# There can be one or many conditions in a 'while' loop 
#       (with or without round brackets)
# The iteration will continue till the 
#       condition returns a True or Truthy value
# 
# 'while' loop can be nested
# Condition returns a boolean value
# Condition compares two values/variables with a 
#       conditional operator
# Conditions return a boolean value
# 
# A condition that returns always True is an infinite loop
# A condition can also be replaced by a boolean
#       while True:
#           # infinite loop
#       while False:
#           # no iteration loop
# RESOURCES
# 


# USAGE:

# while (condition):
#       With round bracket
#       execution block

# while condition:
#       Without round bracket
#       execution block

# while condition or condition:
#       Use with boolean operator - and, or, not
#       execution block

# Defining a blank string
name = ''

# Declaring a while loop with two conditions
#       The loop will keep iterating till the 
#       value of name is either '' or 'aptech'
while (name == '' or name == 'aptech'):
    print('Enter a new name')
    # Getting a new string value for name
    name = input()
    print('Hello ' + str(name))
print('Finished loop')
