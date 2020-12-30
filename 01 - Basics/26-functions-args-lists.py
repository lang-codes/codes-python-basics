# HEAD
# Python Functions - *args
# DESCRIPTION
# Describes
#       capturing all arguments as *args (tuple)
# 
# RESOURCES
#


# Arguments (any number during invocation) can also be 
#       caught as a sequence of arguments - tuple using *args
# Order does matter for unnamed arguments list and makes for 
#       index of argument in list even with *args
# # # Note the * above when passing as argument
#       sequence to function
# Can be named args or any name; it does not matter


def printUnnamedArgs(*args):
    # Note the missing * during access
    print("3. printUnnamedArgs", args)
    for x in enumerate(args):
        print(x)


# Can pass any number of arguments below now
# Follows order of arguments
# Argument's index is the order of arguments passed
printUnnamedArgs([1, 2, 3], [4, 5, 6])

