# HEAD
# Using `with` context block
# DESCRIPTION
# Describes the usage of `with` statement
# RESOURCES
# 

# USAGE
# with expressionObjImplementingEnterExit as aliasObjName:
#   executionStatement

# open is a function that opens a file 
#       using default utf8 encoding
with open("exercises.txt", "r") as fh:
    long_description = fh.read()
print(long_description)

# # Non Working Expression below for Context
# #       Context Manager not implemented using __enter__ and __exit__
# def func():
#     return [1,2,3]

# # Following does not work 
# #       Context Manager not implemented using __enter__ and __exit__
# with func() as f:
#     for i in f:
#         print(i)

# # Following does not work
# #       Context Manager not implemented using __enter__ and __exit__
# f = func()
# with f:
#     for i in f:
#         print(i)