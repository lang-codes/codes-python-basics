# HEAD
# Python Basic Scope Rules - globals and locals key
# DESCRIPTION
# Describes interpretation 
#       difference between global and local scope
# 
# Globally scoping behaviour changes as 
#       soon as there is a local assignation
# Check accessDifferenceOne and accessDifferenceTwo 
#       function
# RESOURCES
# 

# Declaring function that tries to 
#       access globally scoped 'var'
def globallyscoped():
    # below prints 'global'
    print('1. globallyscoped',var)  

# Declaring function that tries to 
#       access locally scoped 'var'
def locallyScoped():
    var = 'local'
    # 'var' prints 'local'
    print('2. locallyScoped',var)  

# Declaring bacon that tries to 
#       access locally scoped 'var'
#       and invokes 'globallyscoped', 'locallyScoped'
#       inside it
def bacon():
    var = 'bacon local'
    # 'var' prints 'bacon local'
    print('bacon fn:',var)  
    globallyscoped()
    locallyScoped()
    # prints 'bacon local'
    print('3. bacon fn:',var) 

# Defining global variable 'var'
var = 'global'

# Invoking bacon that internally invokes
#       globallyscoped and locallyscoped
bacon()

# below prints 'global'
print('4. global scoped ',var) 

# Declaring function that will throw error 
#       since print is done before 
#       assignation of value to locally 
#       scoped variable
def accessDifferenceThree():
    print("5. accessDifferenceThree", var)
    # Complains of "UnboundLocalError:" mentioning using
    # variable 'var' before assignment"
    # The reason is 'global' key was not referred
    #       and the variable is local due to
    #       reassignment
    var = 43

# Defining globally scoped 'var'
var = 42

# Invoking accessDifferenceThree function
accessDifferenceThree()

# ERROR DETAILS -
# Traceback (most recent call last):
#   File "15-local-global-variable-usage.py", line 29, in <module>
#     accessDifferenceThree()
#   File "15-local-global-variable-usage.py", line 24, in accessDifferenceThree
#     print(var) # Complains of "Using variable 'var' before assignment"
# UnboundLocalError: local variable 'var' referenced before assignment

# Printing globally scoped 'var'
# does not get printed due to error
print("6. global scoped ",var)
