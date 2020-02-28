# HEAD
# Classes Introduction - Decorated Properties
# DESCRIPTION
# Describes how to create properties of block
# RESOURCES
# 


class GetterSetter():
    # An class attribute with a getter method is a Property
    attr = "Value"

    # Using @property annotation to 
    #       create property for attr
    @property
    def a(self):
        pass
    
    # Declaring Getter on a for attr
    @a.getter
    def a(self):
        return self.attr
    
    # Declaring Setter on a for attr
    @a.setter
    def a(self):
        return self.attr
    
    # Declaring Deleter on a for attr
    @a.deleter
    def a(self, val):
        del self.attr


obj = GetterSetter()

# Print Values before using setter and direct attribute access
print("obj.attr", obj.attr)

# Use as a setter instead of creating 
#       a .get_attr(self) method and invoking it
print("obj.a", obj.a)

# Use as a setter instead of `obj.attr = 10`
obj.a = 10

# Print Values after using setter and direct attribute access
print("obj.a", obj.a)

# Use as a setter instead of creating 
#       a .get_attr(self) method and invoking it
print("obj.attr", obj.attr)
