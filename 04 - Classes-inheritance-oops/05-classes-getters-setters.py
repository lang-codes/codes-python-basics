# HEAD
# Classes - Getters and Setters
# DESCRIPTION
# Describes how to create getters and setters for attributes
# RESOURCES
# 

# Creating a custom class
# Class name - GetterSetter

class GetterSetter():
    # An class attribute with a getter method is a Property
    attr = "Value"

    # GETTER - gets values for attr
    def get_attr(self):
        return self.attr
    
    # SETTER - sets values for attr
    def set_attr(self, val):
        self.attr = val

obj = GetterSetter()

# Print Values before using setter and direct attribute access
print("obj.get_attr()", obj.get_attr())
print("obj.attr", obj.attr)

# Use a setter
obj.set_attr(10)

# Print Values again using setter and direct attribute access
print("obj.get_attr()", obj.get_attr())
print("obj.attr", obj.attr)
