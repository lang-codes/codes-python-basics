# Describe using of Error Handling of code in python

# 'try' will run always
# 'try' will execute all statements till it encounters an error
#       once an error is encountered, it executes 
#       related except block (named or unnamed)
# 'except' blocks can be named
# Can have any number of named excepts
# There can be only one unnamed except
# You can have or handle multiple 'except' errorhandlers
#       and executing the same except codes
# Means: Can have multiple errors in named excepts,
#       seperated by comma
#           Example
#           except (Err1, Err2, Err3):

# try...except...finally can be used to trigger 
#       'finally' block irrespective
#       of whether an error occured or not


def obj(divideBy):
    return 42 / divideBy


try:
    print(obj(2))
    print(obj(12))
    print(obj(0))
    print(obj(1))
except ZeroDivisionError:  # Catch specific error
    print('Error: Invalid argument.')
finally:
    print('Finally Triggered.')

# try:
#    # do something
#    # execute lines till it meets error, 
#    #      then enters respective except block
#    pass
# except ValueError:
#    # handle ValueError exception
#    pass
# except (TypeError, ZeroDivisionError):
#    # handle multiple exceptions
#    # TypeError and ZeroDivisionError
#    pass
# except:
#    # handle all other exceptions
#    pass
# finally:
#    # executed irrespective of error or not
#     pass
