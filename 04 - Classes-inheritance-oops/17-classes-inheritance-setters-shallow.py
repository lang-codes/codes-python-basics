# HEAD
# Classes - Setters are shallow
# DESCRIPTION
# Describes how setting of inherited attributes and values function
# RESOURCES
# 


# Creating Parent class
class Parent():
    par_cent = "parent"

    # Parent Init method
    def __init__(self, val):
        self.par_cent = val
        print("Parent Instantiated with ", self.par_cent)


# Creating ParentTwo class
class Child(Parent):
    
    # Child Init method
    def __init__(self, val_two):
        print("Child Instantiated with ", val_two)
        
        # Explicit Instantiation of parent init
        # Instantiate parent once and passing args
        #   Parent assigns value storing it in object to access
        #   Parent default value remains
        self.p = super()
        self.p.__init__(val_two)

obj = Child(10)
print("""
    Value of par_cent is assigned & 
    fetched from Child class & 
    default refs of parent remains
""")
print("obj.par_cent", obj.par_cent)
print("obj.p.par_cent, id(obj.p), id(obj)", obj.p.par_cent, id(obj.p), id(obj))

