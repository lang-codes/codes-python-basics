# HEAD
# Python Functions - args, kwargs, *args, **kwargs
# DESCRIPTION
# Describes
#       passing of variables using named arguments,
#       passing of values as names arguments
#       passing of variables as named arguments,
# 
# RESOURCES
#

# Arguments can be passed to functions in declarations/definitions
# Arguments have to be compulsarily passed if
#       declared in definition
# You can have any (no, one, or many) number of arguments definition in a function
# When name of argument is specified with
#       what argument it refers to in terms of
#       function declaration then it is
#       referred to as keyword arguments
# Order does not matter for named keyword arguments
# Arguments can be of any type, can also be a function


# Declares a function hello which takes 'name' as argument
# 'name' can be referred to as a
#       variable inside the function


def hello(name):
    print('1. Hello ' + name)

# IMPLEMENTATION OF INVOCATION SEPARATES ARGUMENTS FROM KEYWORD ARGUMENTS


# keyword arguments - Named arguments
# Named arguments are arguments refering to specific
#       argument in function definition
# Does not follow order of arguments
hello(name="Named Variable - Alice in Wonderland")

def customer(name, age, address):
    print('1. Hello ' + name + str(age), address)


# arguments - Unnamed simple value arguments
# Passing variable as argument during invocation
# Index of specification of arguments passed will be same as ones defined
customer(name="Gary", age=25, address="Bangalore")

city = "Bangalore"
# keyword arguments - Named arguments
# Passing variable as keyword argument during invocation
# Does not follow order of arguments
customer(name="Gary", age=25, address=city)

