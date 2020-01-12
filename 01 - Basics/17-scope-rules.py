# HEAD
# Python Basic Scope Rules
# DESCRIPTION
# Describes scope rules in terms of local and global
# 
# Assignation of variables inside a local 
#       scope makes the variable locally scoped, 
#       even if a global variable is available 
#       in the global scope
# Refer global variables with 'global' key
# Once referred as global with 'global' key, it can 
#       be referred
# RESOURCES
# 



def scoperules():
    global var
    # 'var' is now global reference
    var = 'scoperules'


def bacon():
    # 'var' is now locally scoped since there is 
    #       reassignation
    var = 'bacon' 


def ham():
    # 'var' is the global since there 
    #       is no re-assignment
    print("1. ham", var)


# defining the global variable 'var'
var = 42  

# Invoking scoperules function
scoperules()

# prints scoperules since is global
print("2. global var",var) 

# Invoking bacon
bacon()

# Invoking ham
ham()

# prints scoperules since bacon implements local 
#       variable and doesnt effect var variable
print("3. global var", var)
