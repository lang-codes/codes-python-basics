# Describes
#       passing of variables using arguments,
#       capturing all arguments as *args
#       capturing all arguments as **kwargs

# Arguments can be passed to functions in declarations/definitions
# Arguments have to be compulsarily passed if 
#       declared in definition
# Arguments can be passed as named or 
#       unnamed arguments during invocation
# When name of argument is specified with 
#       what argument it refers to in terms of 
#       function declaration then it is 
#       referred to as keyword arguments
# Order does matter for unnamed arguments
# Order does not matter for named keyword arguments
# Arguments can be of any type, can also be a function
# Default values for arguments can be assigned 
#       in declaration/definition of function


def hello(name):
    print('Hello ' + name)

# IMPLEMENTATION OF INVOCATION SEPARATES ARGUMENTS FROM KEYWORD ARGUMENTS


# arguments - Unnamed simple arguments
hello('Alice')
hello('Wonderland')

# keyword arguments - Named arguments
# Named arguments refering to specific argument in function definition
hello(name="Named Variable - Alice in Wonderland")

# Assigning default values for arguments in definition of function
def helloDefaultValue(name="Default Value"):
    print(name)


# Passed value will be used instead of default
helloDefaultValue("Passed vaue used instead of default value")

# Default value will be used
helloDefaultValue()

# Arguments can also be caught as a sequence of arguments
def printUnnamedArgs(*args):
    print(args)  # Note the missing *
    # printUnnamedArgs(*args)
    # # Note the * above when passing as argument sequence again to function
    for x in enumerate(args):
        print(x)


printUnnamedArgs([1, 2, 3], [4, 5, 6])

# Keyword Arguments can also be caught as a sequence of keyword arguments
def printKeyWordArgs(**kwargs):
    print(kwargs)  # Note the missing **
    # printKeyWordArgs(**kwargs)
    # # Note the ** above when passing as argument sequence again to function
    for k, v in kwargs.items():
        print(k, v)


printKeyWordArgs(a=10, b=20)

# Can pass both *args and **kwargs together
# *args always take precedence in function definition
# Try inverting it or mixing up arguments and keyword arguments in the function
#       to see the behaviour


def fncArgsKwargs(*args, **kwargs):
    print('ARGS: {} and KWARGS: {}'.format(args, kwargs))


fncArgsKwargs(1, 2, 3, a=1, b=2, c=3)

# fncArgsKwargs(c=3, 1,2,3, a=1, b=2)

# Above line of code will throw ERROR
# ERROR DETAILS -
#   File "10-functions-args-kwargs.py", line 48
#     fncArgsKwargs(c=3, 1,2,3, a=1, b=2)
#                       ^
# SyntaxError: positional argument follows keyword argument

# fncArgsKwargs(c=3, 1,2,b=2, 3, a=1)

# Above line of code will throw ERROR
# ERROR DETAILS -
#   File "10-functions-args-kwargs.py", line 56
#     fncArgsKwargs(c=3, 1,2,b=2, 3, a=1)
#                       ^
# SyntaxError: positional argument follows keyword argument

# Try uncommenting the function and invocation then
# try running the inverse definition below -

# def fncArgsKwargsInverse(**kwargs,*args):
#         print('ARGS: {} and KWARGS: {}'.format(args, kwargs))
# 
# fncArgsKwargsInverse(a=1, b=2, c=3, 1,2,3)

# Above line of code will throw ERROR
# ERROR DETAILS -
# fncArgsKwargsInverse will result in following error
#   File "10-functions-args-kwargs.py", line 51
#     def fncArgsKwargsInverse(**kwargs,*args):
#                                       ^
# SyntaxError: invalid syntax
