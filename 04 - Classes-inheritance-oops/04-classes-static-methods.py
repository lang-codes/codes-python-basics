# HEAD
# Classes Introduction - Static Methods
# DESCRIPTION
# Describes how to create static methods in classes
#       Using static methods without instantiation
#       Creating static methods with decorators - Python 3.x
#       Using static methods with instantiation
# RESOURCES
# 


# Creating a custom class
# Class name - MethodDefs

class StaticMethods():
    # An class attribute 
    attribute = "someval"

    # WORKS with instance and FAILS Statically
    def method(self):
        print("Some value")
    
    # WORKS with instance and FAILS Statically
    def method_two(self, a, b):
        return a+b
    
    # FAILS with instance and WORKS Statically
    def method_three(a, b):
        return a+b
    
    # # FAILS with instance and WORKS Statically
    def method_four(a, b):
        # # FAILS accessing self within instance
        # print("FAILS accessing within instance", self.attribute)
        return a+b
    
    # # WORKS with instance and WORKS Statically
    @staticmethod
    def method_five(a, b):
        return a+b


# Accessing a object methods statically

# Following WORKS statically and as an instance
print("Access StaticMethods.method_three(a, b)", StaticMethods.method_three(10, 20))

# Creating a class Instance object
obj = StaticMethods()

# WORKS with Instance but FAILS statically
print("Access obj.method()", obj.method())

# WORKS with Instance but FAILS statically
print("Access obj.method_two(a, b)", obj.method_two(10, 20))

# FAILS with Instance and WORKS Statically
print("Access StaticMethods.method_three(a, b)", StaticMethods.method_three(10, 20))

# # FAILS with Instance and WORKS Statically
# print("Access obj.method_three(a, b)", obj.method_three(10, 20))

# # FAILS with Instance and FAILS Statically
# print("Access StaticMethods.method_four(a, b)", StaticMethods.method_four(10, 20))
# print("Access obj.method_four(a, b)", obj.method_four(10, 20))

# Following WORKS statically and WORKS as an instance
print("Access obj.method_five(a, b)", obj.method_five(10, 20))

# Following WORKS statically and as an instance
print("Access StaticMethods.method_five(a, b)", StaticMethods.method_five(10, 20))

