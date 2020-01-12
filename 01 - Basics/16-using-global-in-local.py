# HEAD
# Python Basic Scope Rules - globals and locals - global key
# DESCRIPTION
# Describe usage of 'global' key
# RESOURCES
# 

# 'global' key is used to reference a variable 
#       usage or definition in global context 
#       within a local scope; whichever applies


def myfunc():
    # Referencing to global 'var'
    global var
    # printing the globally referenced 'var'
    print("1. global referenced var", var)
    # Linter Complains of "Using variable 'var' 
    #       before assignment"
    #       but code works
    
    # Reassigning globally scoped 'var' with str 'myfunc'
    var = 'myfunc'

# Defining a global variable 'var'
var = 'global'

# Invoking the function
myfunc()

# Check if var is globally defined
# It is global in this case
print("2. global var", var)
