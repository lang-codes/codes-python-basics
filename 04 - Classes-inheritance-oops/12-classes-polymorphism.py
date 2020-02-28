# HEAD
# Classes - Polymorphism
# DESCRIPTION
# Describes how to create polymorphism using classes
# RESOURCES
# 


# Creating Parent class
class Parent():
    par_cent = "parent"
    
    def p_method(self):
        print("Parent Method invoked with par_cent", self.par_cent)
        return self.par_cent


# Inheriting all Parent attributes 
#       and methods into Child
# Form ONE
class ChildOne(Parent):
    chi_one_cent = "childtwo"
    
    def c_one_method(self):
        print("Child Method invoked with chi_one_cent", self.chi_one_cent)
        
        # Accessing Parent methods
        return self.chi_one_cent, self.p_method()


# Inheriting all Parent attributes 
#       and methods into Child
# Form TWO
class ChildTwo(Parent):
    chi_two_cent = "child"
    
    def c_two_method(self):
        print("Child Method invoked with chi_two_cent", self.chi_two_cent)
        
        # Accessing Parent methods
        return self.chi_two_cent, self.p_method()


obj = ChildOne()
# Access/Invoke Parent and Child Attributes, Methods
print("obj.par_cent ", obj.par_cent)
print("obj.chi_one_cent ", obj.chi_one_cent)
print("obj.p_method ", obj.p_method())
print("obj.c_one_method ", obj.c_one_method())


obj_two = ChildTwo()
# Access/Invoke Parent and Child Attributes, Methods
print("obj_two.par_cent ", obj_two.par_cent)
print("obj_two.chi_two_cent ", obj_two.chi_two_cent)
print("obj_two.p_method ", obj_two.p_method())
print("obj_two.c_two_method ", obj_two.c_two_method())

