# HEAD
# Python Basic Scope - local variables
# DESCRIPTION
# Declaring a local variable inside a 
#       local scope of a function
# 
# Locally scoped variables cannot be accessed outside
#       the local scope; in this case the function
# Functions create a local scope and a execution 
#       block context
# RESOURCES
# 



# Implementation of local scope of 'mylocalvar'

def obj():
    # Value assigned inside function
    # hence mylocalvar is local 
    mylocalvar = 99
    bacon()
    print(mylocalvar)

# Another local scope of 'ham' and 'mylocalvar'

def bacon():
    ham = 101
    mylocalvar = 0

obj()

def name():
    # Value assigned inside function
    # hence mylocalvar is local 
    mylocalvar = 10

print(mylocalvar)  # Will throw ValueError

# ERROR DETAILS -
# Traceback (most recent call last):
#   File "13-local-variables.py", line 21, in <module>
#     print(mylocalvar) # Will throw ValueError
# NameError: name 'mylocalvar' is not defined
