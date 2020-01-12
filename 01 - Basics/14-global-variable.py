# HEAD
# Python Basic Scoped Variables
# DESCRIPTION
# Describes the creation of globally scoped variable
# 
# global scope variables are defined in the 
#       root level of script/process
# global scope variables are available to any scope
# Pass globally scoped variables as arguments 
#       for use within function, incase
#       you face a problem accessing globally scoped variables.
#       In such a case, it will be local scope and
#       will be reference of a variable within the function
# However, globally scoping behaviour changes 
#       as soon as there is a local assignation
# RESOURCES
# 



# Check accessDifferenceOne and accessDifferenceTwo function


def accessGlobalVariableAsArgument():
    print(var)  # global scoped access of var since no assignation in function


var = 42
accessGlobalVariableAsArgument()
print(var)


def passGlobalVariableAsArgument(var):
    print(var)  # global scoped access of var since no assignation in function


var = 42
passGlobalVariableAsArgument(var)
print(var)


def accessDifferenceOne():
    var = 43  # Now locally scoped
    print(var)


var = 42
accessDifferenceOne()
print(var)


def accessDifferenceTwo(var):
    var = 43  # Now locally scoped and not global
    print(var)


var = 42
accessDifferenceTwo(var)
print(var)
