# HEAD
# Python Functions - args, kwargs, *args, **kwargs
# DESCRIPTION
# Describes
#       passing of variables using arguments,
#       passing of values as arguments
#       passing of variables as arguments,
#       capturing all arguments as *args (tuple)
#       capturing all arguments as **kwargs (dictionary)
# RESOURCES
# 

# Arguments can be passed to functions in declarations/definitions
# Arguments have to be compulsarily passed if 
#       declared in definition
# You can pass any (no, one, or many) arguments to a function
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

# Declares a function hello which takes 'name' as argument
# 'name' can be referred to as a 
#       variable inside the function
def hello(name):
    print('1. Hello ' + name)

# IMPLEMENTATION OF INVOCATION SEPARATES ARGUMENTS FROM KEYWORD ARGUMENTS

# arguments - Unnamed simple value arguments
hello('Alice')
hello('Wonderland')

# keyword arguments - Named arguments
# Named arguments refering to specific 
#       argument in function definition
hello(name="Named Variable - Alice in Wonderland")

# Assigning default values for arguments 
#       in definition of function
def helloDefaultValue(name="Default Value"):
    print('2. helloDefaultValue ' + name)

# Passed value will be used instead of default
helloDefaultValue("Passed vaue used instead of default value")

# Default value of argument will be used
helloDefaultValue()

# Arguments can also be caught as a sequence of arguments - tuple
# # Note the * above when passing as argument 
#       sequence to function
# Can be named args or any name; it does not matter
def printUnnamedArgs(*args):
    # Note the missing * during access
    print("3. printUnnamedArgs",args) 
    for x in enumerate(args):
        print(x)

# Can pass any number of arguments below now
printUnnamedArgs([1, 2, 3], [4, 5, 6])

# Keyword Arguments can also be caught as a 
#       map of keyword arguments - dictionary
# # Note the ** when passing as keyword argument 
#       map to function
# Can be named kwargs or any name; it does not matter
def printKeyWordArgs(**kwargs):
    # Note the missing ** during access
    print(kwargs)  
    for k, v in kwargs.items():
        print(k, v)

# Can pass any number of keyword arguments below now
printKeyWordArgs(a=10, b=20)

# Can pass both *args and **kwargs together
# *args always take precedence in function definition
# Try inverting it or mixing up arguments and keyword arguments in the function
#       to see the behaviour

def fncArgsKwargs(*args, **kwargs):
    print('ARGS: {} and KWARGS: {}'.format(args, kwargs))


# BELOW WORKS: 
# Passing arguments at first in order and 
#       keyword arguments later
fncArgsKwargs(1, 2, 3, a=1, b=2, c=3)



# BELOW FAILS: 
# Passing keyword argument first then 
#       arguments in order and other 
#       keyword arguments later
# Try uncommenting the following invocation then
#       try running again

# fncArgsKwargs(c=3, 1,2,3, a=1, b=2)

# # Above line of code will throw ERROR
# ERROR DETAILS -
#   File "10-functions-args-kwargs.py", line 48
#     fncArgsKwargs(c=3, 1,2,3, a=1, b=2)
#                       ^
# SyntaxError: positional argument follows keyword argument



# BELOW FAILS: 
# Passing keyword arguments and 
#       arguments in a jumbled and unordered manner
# Try uncommenting the following invocation then
#       try running again

# fncArgsKwargs(c=3, 1,2,b=2, 3, a=1)

# # Above line of code will throw ERROR
# ERROR DETAILS -
#   File "10-functions-args-kwargs.py", line 56
#     fncArgsKwargs(c=3, 1,2,b=2, 3, a=1)
#                       ^
# SyntaxError: positional argument follows keyword argument



# BELOW FAILS: 
# Try uncommenting the function and invocation then
#       try running the inverse definition below -

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
