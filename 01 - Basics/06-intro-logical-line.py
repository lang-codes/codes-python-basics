# HEAD
# Python Basics - Logical Line
# DESCRIPTION
# Describes what is a logical line 
# Describes how logical can be broken into two lines which 
#       together makes a single logical line
# 
# RESOURCES
# 

# One Logical Line completes an operation and 
#    and is standalone statement
print("This whole line with the print function keyword is a logical line")

# The whole assignment of value 'test' to target password is One Logical Line
password = "test"

# One Logical Line but incorrect continuation of block after : hence it will err out
# if password == 'swordfish':

# One Logical Line broken into two using a backslash \
if password == \
     'swordfish':
    print('Access granted.')

password = \
     "test"

