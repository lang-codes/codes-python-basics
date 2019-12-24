# Describes a list and working with its elements

# List is a sequence, iterator that can 
#       contain any type of items in it
# A list can also have lists or tuples in them
# A list is mutable, which means its items 
#       can be changed or modified
# A list behaves like array of other programming language
# A list is created using [] or square brackets
# A list item can be referenced by a index 
#       and the indexing starts with 0/zero
# A list can be iterated or looped using 
#       'for' or 'while' loops


# Simple list created using [] brackets
lists = ['cat', 'bat', 'rat', 'elephant']
print(lists)

# Referencing items
print(lists[1]) # 'bat'
print(lists[-1]) # 'elephant'

# Simple list assignation
nums = [1,2,3,4,5]
print(nums)

print(nums[0]) # 1
print(nums[-1]) # 5

# Referencing items using range

# USAGE
# list[start:end]
print(lists[1:4]) # [bat', 'rat']
print(lists[:4]) # ['cat', 'bat', 'rat']

# Referencing items using range start but without end range 
# (defaults to last item of list)
print(lists[1:]) # [bat', 'rat', 'elephant']

# Referencing items using range start but without end range 
# (defaults to first item of list)
print(lists[:2]) # [bat', 'rat', 'elephant']

# Referencing items using range but without start and end range
# (defaults to first and last item of list)
print(lists[:]) # [bat', 'rat', 'elephant']

listOfLists = [['cat', 'bat', 'rat', 'elephant'], [1,2,3,4,5]]

# Referencing items of inner list items
# Second bracket refers to inner list or sequence
# Range also works in the same way, as for a simple list
print(listOfLists[0][1]) # 'bat'
print(listOfLists[1][1]) # 2

# len() function provides the length of list
print(len(lists))
print(len(nums))
