# HEAD
# Python Functions - Accessing globals using the global key
# DESCRIPTION
#       Describes how to
#           - create global reference for variables
#           - assign values to global variables even from local context 
# 
# RESOURCES
#


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
    # Following name variable is a global variable
    #       since a value is assigned within a function
    #       but a global key is defined
    global name
    name = "hello_global: Local Var accessor 'name' with global key reference"
    print('hello_global: Hello there.')
    print(name)
    print("hello_global: Object id of local variable 'name' with global key reference.")
    print(id(name))
    # This is global name accessed as global_name
    print("hello_global: This is global variable 'global_name' passed as local function definition argument.")
    print(global_name)
    print("hello_global: Object id of local variable 'global_name' passed as local function definition argument.")
    print(id(global_name))

# Passing global 'name' variable which is assigned to global_name
hello_global(name)
print("global: Object id of global variable name now will have changed value.")
print(id(name))

