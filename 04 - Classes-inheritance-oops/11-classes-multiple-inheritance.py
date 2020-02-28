# HEAD
# Classes - Multiple Inheritance
# DESCRIPTION
# Describes how to create multiple inheritance using classes
# RESOURCES
# 


# Creating Parent class
class Parent():
    par_cent = "parent"
    
    def p_method(self):
        print("Parent Method invoked with par_cent", self.par_cent)
        return self.par_cent


# Creating Parent Two class
class ParentTwo():
    par_two_cent = "parenttwo"
    
    def p_two_method(self):
        print("Parent Two Method invoked with par_two_cent", self.par_two_cent)
        return self.par_two_cent


# Inheriting all Parent attributes 
#       and methods into Child
class Child(Parent, ParentTwo):
    chi_cent = "child"
    
    def c_method(self):
        print("Child Method invoked with chi_cent", self.chi_cent)
        
        # Accessing Parent methods
        return self.p_method(), self.p_two_method()


obj = Child()


# Access Parent and Child Attributes
print("obj.par_cent ", obj.par_cent)
print("obj.par_two_cent ", obj.par_two_cent)
print("obj.chi_cent ", obj.chi_cent)


# Invoke Parent and Child Methods
print("p_method ", obj.p_method())
print("p_two_method ", obj.p_two_method())
print("c_method ", obj.c_method())

