# HEAD
# Classes - Metaclasses Introduction
# DESCRIPTION
# Describes how to work with metaclasses
# RESOURCES
# 


# Custom Metaclass declaration
class Meta(type):
    pass

# Custom Class applying metaclass
class CustomClass(metaclass=Meta):
    attr = "CustomClass"
    def __init__(self):
        print("self.attr", self.attr)

# Custom Class applying metaclass
class CustomClassWithParent(CustomClass, metaclass=Meta):
    cAttr = "CustomClassWithParent"
    def __init__(self):
        print("self.cAttr", self.cAttr)


# Instanting class with metaclass
o = CustomClass()

# Custom Class with parent applying metaclass
c = CustomClassWithParent()
