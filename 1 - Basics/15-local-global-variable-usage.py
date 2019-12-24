# Describes interpretation 
#       difference between global and local scope

# Globally scoping behaviour changes as 
#       soon as there is a local assignation

# Check accessDifferenceOne and accessDifferenceTwo function


def globalSpam():
    print(var)  # prints 'spam global'


def locallyScoped():
    var = 'spam local'
    print(var)  # prints 'spam local'


def bacon():
    var = 'bacon local'
    print(var)  # prints 'bacon local'
    globalSpam()
    locallyScoped()
    print(var)  # prints 'bacon local'


var = 'global'
bacon()
print(var)  # prints 'global'


def accessDifferenceThree():
    print(var)
    # Complains of "UnboundLocalError:" mentioning using
    # variable 'var' before assignment"
    var = 43

    # Will throw error since print is done before assignation
    # of value to locally scoped variable
var = 42
accessDifferenceThree()

# ERROR DETAILS -
# Traceback (most recent call last):
#   File "15-local-global-variable-usage.py", line 29, in <module>
#     accessDifferenceThree()
#   File "15-local-global-variable-usage.py", line 24, in accessDifferenceThree
#     print(var) # Complains of "Using variable 'var' before assignment"
# UnboundLocalError: local variable 'var' referenced before assignment

print(var)
