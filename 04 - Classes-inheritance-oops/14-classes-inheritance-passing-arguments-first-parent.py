# HEAD
# Classes Inheritance & super() - passing arguments for First Parents
# DESCRIPTION
# Describes how to pass arguments to first parent using super
# RESOURCES
# 


# Creating Parent class
class Parent():
    par_cent = "parent"

    # Parent Init method
    def __init__(self, val):
        self.par_cent = val
        print("Parent Instantiated")
    
    def p_method(self):
        print("Parent Method invoked with par_cent", self.par_cent)
        return self.par_cent


# Inheriting all Parent attributes 
#       and methods into Child
class Child(Parent):
    chi_one_cent = "childtwo"
    
    # Child Init method
    def __init__(self, val):
        self.chi_one_cent = val
        print("Child Instantiated")
        
        # # Alternative implementation to 
        # #       invoke/execute parent init
        # # Passing arguments to first parent
        super().__init__(val)

    def c_one_method(self):
        print("Child Method invoked with chi_one_cent", self.chi_one_cent)
        
        # Accessing Parent methods
        return self.chi_one_cent, self.p_method()


obj = Child(10)
