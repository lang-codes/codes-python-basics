# Declaring a local variable inside a 
#       local scope of a function

# locally scoped variables cannot be accessed outside
#       the local scope; in this case the function
# Functions create a local scope and a execution 
#       block context

# Implementation of local scope of 'eggs'


def obj():
    eggs = 99
    bacon()
    print(eggs)

# Another local scope of 'ham' and 'eggs'


def bacon():
    ham = 101
    eggs = 0


obj()


def name():
    eggs = 10


print(eggs)  # Will throw ValueError

# ERROR DETAILS -
# Traceback (most recent call last):
#   File "13-local-variables.py", line 21, in <module>
#     print(eggs) # Will throw ValueError
# NameError: name 'eggs' is not defined
