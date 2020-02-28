# HEAD
# Classes Introduction - Creating Attributes and objects from classes
# DESCRIPTION
# Describes how to create attributes
#       Use classes to create objects with your attributes
# RESOURCES
# 


# Creating a custom class
# Class name - AttributeDefs

class AttributeDefs():
    # Simple public class attribute
    # attributes follows all rules of variables 
    #       like definition, naming, usage rules
    attribute = "value"

    # Second attribute
    # seperate two words with underscore - snake case
    sec_attribute = "someothervalue"


# Creating a class instance object
obj = AttributeDefs()

# Accessing a object attributes
print("Access obj.attribute", obj.attribute)
print("Access obj.sec_attribute", obj.sec_attribute)

