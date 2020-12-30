# HEAD
# Python Functions - Accessing globals
# DESCRIPTION
#       Describes how to
#           - create global variables
#           - pass global variable as a copy to local variable during
#                   invocation
# 
# RESOURCES
#


name = "Global Var accessor"
# Defining a function called hello
# Access of variable directly inside function
def hello():
    print('hello: Direct Access of global variable: Hello there.')
    print(name)
    print("hello: Object id of locally accessed global variable name.")
    print(id(name))

hello()
print("global: Object id of global variable name.")
print(id(name))


# Defining a function called hello
# Passing of global variable using function invocation
def hello_variable(varname):
    print('hello_variable: InDirect Global Access by passage through function invocation: Hello there.')
    print(varname)
    print("hello_variable: global: Object id of local variable varname.")
    print(id(varname))

hello_variable(name)
print("global: Object id of global variable name.")
print(id(name))

