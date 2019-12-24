# Decribes how copy works with copy module

import copy
spam = ['A', 'B', 'C', 'D']

# Applying simple copy
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
# ['A', 'B', 'C', 'D']
print(cheese)
# ['A', 42, 'C', 'D']
