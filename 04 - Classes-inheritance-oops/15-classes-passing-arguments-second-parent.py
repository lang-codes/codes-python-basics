# HEAD
# Classes Inheritance & passing arguments to Second Parent
# DESCRIPTION
# Describes how to pass arguments to second parent onwards using instantiation
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
class ParentTwo():
    par_two_cent = "parent"

    # Parent Init method
    def __init__(self, val_two):
        self.par_two_cent = val_two
        print("ParentTwo Instantiated with ", self.par_two_cent)


# Inheriting all Parent attributes 
#       and methods into Child
class Child(Parent, ParentTwo):
    chi_one_cent = "childtwo"

    # Child Init method
    def __init__(self, val, val_two):
        print("Child Instantiated with args ", val, val_two)

        # # Passing arguments to first parent - Parent
        super().__init__(val)
        # # Passing arguments to second parent - ParentTwo
        ParentTwo.__init__(self, val_two)


obj = Child(10, 20)

