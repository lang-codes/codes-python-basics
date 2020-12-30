# HEAD
# Python Functions - Returning values
# DESCRIPTION
#       Describes how to
#           - create function with no retun value
#           - create function with retun value
# 
# RESOURCES
#


# Defining a function called hello with no return value
# If no return is specified the the default return value of
#       function is None
def hello():
    print('hello: Hello there.')


# No return value provides None
return_value = hello()
print("Return value not provided:", return_value)


# Defining a function called hello with blank return value
# If blank return is specified the the default return value of
#       function is None
def hello_blank_return():
    print('hello_blank_return: Hello there.')
    return


# No return value provides None
return_value = hello_blank_return()
print("Return value not provided:", return_value)


# Defining a function called hello_return with return value
def hello_return():
    print('hello_return: Hello there.')
    return "My any return value"


# No return value provides value defined
return_value = hello_return()
print("Return value provided:", return_value)

