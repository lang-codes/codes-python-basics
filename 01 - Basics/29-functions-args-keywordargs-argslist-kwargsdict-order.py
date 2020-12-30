# HEAD
# Python Functions - args, kwargs, *args, **kwargs
# DESCRIPTION
# Describes
#       capturing all arguments as *args (tuple), 
#               and **kwargs (dictionary) together
#       capturing all arguments with default arg 
#               definition, *args (tuple), and **kwargs 
#               (dictionary) together
# 
# RESOURCES
#


# # PASSING *args AND **kwargs TOGETHER
# Can pass both *args and **kwargs together
# *args always take precedence in function definition
# *kwargs always are after in function definition
# *args and **kwargs are always last in function definition
# Default arguments defined should be before *args 
#           and **kwargs in function definition
# Try inverting it or mixing up arguments and 
#           keyword arguments in the function
#           to see the behaviour


def fncArgsKwargs(*args, **kwargs):
    print('ARGS: {} and KWARGS: {}'.format(args, kwargs))


# BELOW WORKS:
# Passing arguments at first in order and
#       keyword arguments later
fncArgsKwargs(1, 2, 3, a=1, b=2, c=3)


# # BELOW FAILS:
# # Passing keyword argument first then
# #       arguments in order and other
# #       keyword arguments later
# # Try uncommenting the following invocation then
# #       try running again

# fncArgsKwargs(c=3, 1,2,3, a=1, b=2)

# # Above line of code will throw ERROR
# ERROR DETAILS -
#   File "10-functions-args-kwargs.py", line 48
#     fncArgsKwargs(c=3, 1,2,3, a=1, b=2)
#                       ^
# SyntaxError: positional argument follows keyword argument


# # BELOW FAILS:
# # Passing keyword arguments and
# #       arguments in a jumbled and unordered manner
# # Try uncommenting the following invocation then
# #       try running again

# fncArgsKwargs(c=3, 1,2,b=2, 3, a=1)

# # Above line of code will throw ERROR
# ERROR DETAILS -
#   File "10-functions-args-kwargs.py", line 56
#     fncArgsKwargs(c=3, 1,2,b=2, 3, a=1)
#                       ^
# SyntaxError: positional argument follows keyword argument


# # BELOW FAILS:
# # Try uncommenting the function and invocation then
# #       try running the inverse definition below -

# def fncArgsKwargsInverse(**kwargs,*args):
#         print('ARGS: {} and KWARGS: {}'.format(args, kwargs))

# fncArgsKwargsInverse(a=1, b=2, c=3, 1,2,3)

# Above line of code will throw ERROR
# ERROR DETAILS -
# fncArgsKwargsInverse will result in following error
#   File "10-functions-args-kwargs.py", line 51
#     def fncArgsKwargsInverse(**kwargs,*args):
#                                       ^
# SyntaxError: invalid syntax

# # PASSING ARGUMENT WITH DEFAULT VALUE, *args, AND **kwargs TOGETHER
def fncDefaultArgsArgsKwargs(kw="default args", *args, **kwargs):
    print('ARGS: {} and KWARGS: {}'.format(args, kwargs))


# Normal invocation passing args and kwargs
# kw is assigned with the first argument (value: 1)
fncDefaultArgsArgsKwargs(1, 2, 3, a=1, b=2, c=3)


# Normal invocation passing args and kwargs
# kw is assigned with the first argument (kw=3)
fncDefaultArgsArgsKwargs(kw=3, a=1, b=2, c=3)


# # Normal invocation passing args and kwargs
# # kw is assigned with the first argument and cannot be passed later
# fncDefaultArgsArgsKwargs(1, 2, kw=3, a=1, b=2, c=3)

