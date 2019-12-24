# Describes the assigning, working, and method usages of sets
# Frozenset will not manipulator functions since they are immutable

# Using the set function to create a blank set
set1 = set()
print("Intial blank Set: ") 
print(set1)

# Adding elements to the Set in a simple fashion or using for...in loops 
set1.add(8) 
set1.add(9) 
set1.add(12) 
print("\nSet after Addition of Three elements: ") 
print(set1) 

# Addition of elements to the Set 
# using Update function 
set1.update([10, 11]) 
print("\nSet after Addition of elements using Update: ") 
print(set1)

# Removing elements from Set 
# using Remove() method 
set1.remove(10) 
print("\nSet after Removal of one elements: ") 
print(set1)

# Removing elements from Set 
# using Discard() method 
set1.discard(12) 
print("\nSet after Discarding two elements: ") 
print(set1)

# Removing element from the  
# Set using the pop() method 
set1.pop() 
print("\nSet after popping an element: ") 
print(set1)

# Removing all the elements from  
# Set using clear() method 
set1.clear()
print("\nSet after clearing all the elements: ") 
print(set1)