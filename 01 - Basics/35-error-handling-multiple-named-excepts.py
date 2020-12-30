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
# Can have any number of named excepts
# There can be only one unnamed except (and in the end)
# Named Except or Unnamed Except are optional but
#       one except with try block is compulsory
# You can have or handle multiple 'except' errorhandlers
#       and execute its except codes
# Means: Can have multiple errors in named excepts,
#       seperated by comma
#           Example
#           except (Err1, Err2, Err3):

# try...except Exception...except Exception...except can be used to
#        invoke a set of statements


def obj(divideBy):
    return 42 / divideBy


try:
    # do something
    # execute lines till it meets error,
    #      then enters respective except block
    print(obj(2))
    print(obj(0))
except ValueError:
    # handle ValueError exception
    print("Value Error handler")
except (TypeError, ZeroDivisionError):
    # handle multiple exceptions
    # TypeError and ZeroDivisionError
    print("TypeError or ZeroDivision Error handler")
except:
    # handle all other exceptions
    print("Unhandled Error Exception handler")
