# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Decribes how deepcopy works with copy module
# RESOURCES
# 

import copy

# copy copies the reference of lists inside the lists
spam = [[[7,8,9,0],2,3,4,5], 'B', 'C', 'D']

# Applying simple copy
cheese = copy.copy(spam)
cheese[0][1] = 42
cheese[3] = 42
print(spam)

# RESULT:
# ['A', 'B', 'C', 'D']
print(cheese)
# RESULT:
# ['A', 42, 'C', 'D']
cheese[0][1] = 2

# deepcopy copies the lists inside the lists and 
#       not reference of the lists inside lists
# Applying simple copy
cheeseDeepCopy = copy.deepcopy(spam)
print(spam)
print(cheeseDeepCopy)
# RESULT:
# [[1,2,3,4,5], 'B', 'C', 'D']
cheeseDeepCopy[0][1] = 9
print(spam)
print(cheeseDeepCopy)
# RESULT:
# [[1,9,3,4,5], 'B', 'C', 'D']
