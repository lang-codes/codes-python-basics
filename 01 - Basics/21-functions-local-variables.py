# HEAD
# Python Functions - Accessing locals
# DESCRIPTION
#       Describes how to
#           - create local variables
#           - create local variables with same name as global variable
#           - pass global variable as a copy to local variable during
#                   invocation
# 
# RESOURCES
#


# Defining a function called my_local
# Creation of local variable directly inside function
def my_local():
    localvar = "Local variable"
    print("my_local: Hello there.")
    print(localvar)


name = "Global Var accessor"
# Defining a function called hello
# Access of local variable directly inside function
def hello():
    # Following name variable is a local variable
    #       since a value is assigned within a function
    name = "Local Var accessor now"
    print('hello: Hello there.')
    # This is local variable 'name' not global variable 'name'
    print(name)
    print("hello: Object id of local variable name.")
    print(id(name))

hello()

# Access of global variable directly outside function
print("Global variable name accessed from global scope", name)
print("global: Object id of global variable name.")
print(id(name))


# Defining a function called hello_global
# Passage of global as local variable definition in function
def hello_global(global_name):
    # Following name variable is a local variable
    #       since a value is assigned within a function
    name = "Local Var accessor"
    print('hello_global: Hello there.')
    print(name)
    print("hello_global: Object id of local variable name.")
    print(id(name))
    # This is global name accessed as global_name
    print("hello_global: This is global passed as local.")
    print(global_name)
    print("hello_global: Object id of local variable global_name passed as local.")
    print(id(global_name))

# Passing global 'name' variable which is assigned to global_name
hello_global(name)
print("global: Object id of global variable name.")
print(id(name))

