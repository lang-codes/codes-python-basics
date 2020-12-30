# HEAD
# Python Functions - **kwargs
# DESCRIPTION
# Describes
#       capturing all arguments as **kwargs (dictionary)
# 
# RESOURCES
#


# Keyword Arguments (any number during invocation) can also be 
#       caught as a map of keyword arguments - dictionary using **kwargs
# Order does not matter for named keyword arguments even with **kwargs
# # Note the ** when passing as keyword argument
#       map to function
# Can be named kwargs or any name; it does not matter


def printKeyWordArgs(**kwargs):
    # Note the missing ** during access within function
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


# Can pass any number of keyword arguments below now
printKeyWordArgs(a=10, b=20)

