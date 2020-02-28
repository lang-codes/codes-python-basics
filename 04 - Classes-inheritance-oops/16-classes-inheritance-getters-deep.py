# HEAD
# Classes - Getters are deep
# DESCRIPTION
# Describes how getters of inherited attributes and values function
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
        print("ParentTwo Instantiated with ", val_two)
        
        # No Explicit Instantiation of parent init
        self.p = super()


obj = Child(10)

print("""
    Value of par_cent is not assigned on obj 
    & fetched from Parent class attribute
""")
print("obj.par_cent", obj.par_cent)
print("obj.p.par_cent, id(obj.p), id(obj)", obj.p.par_cent, id(obj.p), id(obj))

