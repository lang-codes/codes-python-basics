# HEAD
# Python Functions - args, kwargs, *args, **kwargs
# DESCRIPTION
# Describes
#       passing of variables using arguments,
#       passing of values as arguments
#       passing of variables as arguments,
# 
# RESOURCES
#

# Arguments can be passed to functions in declarations/definitions
# Arguments have to be compulsarily passed if
#       declared in definition
# You can have any (no, one, or many) number of arguments definition in a function
# Order does matter for unnamed arguments
# Arguments can be of any type, can also be a function

# Declares a function hello which takes 'name' as argument
# 'name' can be referred to as a
#       variable inside the function


def hello(name):
    print('1. Hello ' + name)

# IMPLEMENTATION OF INVOCATION SEPARATES ARGUMENTS FROM KEYWORD ARGUMENTS


# arguments - Unnamed simple value arguments
hello('Alice')
hello('Wonderland')


def customer(name, age, address):
    print('1. Hello ' + name + str(age), address)

# arguments - Unnamed simple value arguments
# Follows order of arguments
customer("Gary", 25, "Bangalore")


city = "Bangalore"
# arguments - Unnamed simple value arguments
# Passing variable as argument during invocation
# Index of specification of arguments passed will be same as ones defined
customer("Gary", 25, city)

