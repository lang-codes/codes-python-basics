# HEAD
# Python Error Handling - UnNamed Excepts
# DESCRIPTION
# Describes using of Error Handling of code in python
# try...except is used for error handling
# RESOURCES
# 

# 'try' block will be be executed by default
# If an error occurs then the specific or 
#       related 'except' block will be trigered
#       depending on whether the 'except' block 
#       has named error or not
# 'except' can use a named error and have multiple errors
# 'except' without name will handle and 
#       execute if any error occurs
# You can have any number of 'except' blocks


def obj(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
    except (TypeError, NameError):
        print('Error: Multiple Error Block.')
    except:
        print('Error: Invalid argument.')

print(obj(2))
print(obj(12))
# Will throw ZeroDivisionError and will be 
#       captured triggering respective except block
print(obj(0))
print(obj(1))

# # Error Handling using ImportError
# try:
# # Non-existent module
#     import def
# except ImportError:
#     print('Module not found')