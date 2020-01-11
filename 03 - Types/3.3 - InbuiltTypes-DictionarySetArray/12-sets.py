# Describes the assigning, working, and method usages of sets
# Frozenset will not manipulator functions since they are immutable

# Set is an unordered collection of data type
# that is iterable, mutable and has no duplicate elements

# Frozen sets in Python are "immutable" objects that only support methods 
# and operators that produce a result without affecting the frozen set or 
# sets to which they are applied

# Creating a Set 
set1 = set() 
print("Intial blank Set: ") 
print(set1) 

# Creating a Set with 
# the use of a List 
set2 = set(["Geeks", "For", "Geeks"]) 
print("\nSet with List: ") 
print(set2) 

# Creating a Set with  
# a mixed type of values 
# (Having numbers and strings) 
set3 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print("\nSet with Mixed Values") 
print(set3)

# Creating a frozen Set 
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r') 
Fset1 = frozenset(String) 
print("The FrozenSet is: ") 
print(Fset1) 