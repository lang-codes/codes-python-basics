# HEAD
# Classes Introduction - Methods
# DESCRIPTION
# Describes how to create methods in classes
#       Use classes to create objects with own methods
# RESOURCES
# 


# Creating a custom class
# Class name - MethodDefs

class MethodDefs():
    # Simple public method doing just printing
    # 
    # Method follows all rules of functions
    # Method has first argument always as self - reference 
    #       to internal reference of instance
    def method(self):
        print("Some value")
    
    # Using snake case to declare two word methods
    def method_two_names(self):

        # Single return value
        return "Some Value"
    
    # Passing args and args w/default value like functions
    def method_three(self, a1, a2, a3="DefaultValue"):
        # Access all arguments as seperate values inside method
        #
        # Printing all args a1, a2, a3
        #
        # a3 will use "DefaultValue" when args 
        #       during invocation not passed
        # a3 will use arg value used during 
        #       invocation when args during 
        #       invocation passed
        print("a1, a2, a3", a1, a2, a3)

        # Multiple return values
        return "Multiple Returns", a1, a2, a3

    # Passing *args as tuple like functions
    def method_four(self, *args):
        # Access *args using args name
        # Printing args and type of args
        print("*args", args, type(args))

        # do any operation here
        return "Some Value"

    # Passing **kwargs as dict like functions
    def method_five(self, **kwargs):
        return "Some Value"

    # Passing *args, and **kwargs as dict like functions
    def method_six(self, *args, **kwargs):
        return "Some Value"
    
    # Passing a mix like functions
    def method_seven(self, a1, a2, a3="Default Value", *args, **kwargs):
        return "Some Value"


# Creating a class instance object
obj = MethodDefs()

# Accessing a object methods using invocation
print("Access obj.method()", obj.method())
print("Access obj.method_two_names()", obj.method_two_names())

# Passing as simple args - simple values
#       (ignore self argument during invocation)
print("Access obj.method_three()", obj.method_three(10, 20, 30))

# Passing as simple args - simple values
#   Skipping a3 during invocation 
#       - default value provided during declaration gets applied
#       - ignore self argument during invocation
print("Access obj.method_three()", obj.method_three(10, 20))

