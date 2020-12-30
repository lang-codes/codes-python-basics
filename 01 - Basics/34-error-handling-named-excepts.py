# HEAD
# Error Handling - using Named Exceptions in excepts
# DESCRIPTION
# Describe using of Error Handling of code in python
# 
# RESOURCES
#

# 'try' will run always
# 'try' will execute all statements till it encounters an error
#       once an error is encountered, it executes
#       related except block (named or unnamed)
# 'except' blocks can be named
# Named Except or Unnamed Except are optional but
#       one except with try block is compulsory
# There can be only one unnamed except (and in the end)

# try...except Exception...except can be used to trigger


def obj(divideBy):
    return 42 / divideBy


try:
    print(obj(2))
    print(obj(12))
    print(obj(0))
    print(obj(1))
except ZeroDivisionError:
    # Catch specific error
    print('Error: Invalid argument.')


try:
    print(obj(2))
    print(obj(12))
    print(obj(0))
    print(obj(1))
except:
    # Catch specific error
    print('Error: Invalid argument.')


try:
    print(obj(2))
    print(obj(12))
    print(obj(0))
    print(obj(1))
except ZeroDivisionError:
    # Catch specific error
    print('Error: Invalid argument.')
except:
    print('Except Triggered.')


# # Following will fail with an error
# # Either a named except has to be there or
# #       an unnamed except has to be there
# try:
#     print(obj(2))
#     print(obj(12))
#     print(obj(0))
#     print(obj(1))
