# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes a tuple and working with its elements
# Tuple is a sequence, iterator that can contain any type of items in it
# A tuple can also have tuples or lists in them
# A tuple is immutable, which means its items cannot be changed or modified
# A tuple behaves like array of other programming language
# A tuple is created using () or round brackets
# A tuple item can be referenced by a index and the indexing starts with 0/zero
# A tuple can be iterated or looped using 'for' or 'while' loops
# RESOURCES
# 

# Simple list created using () brackets
eggs = ('hello', 42, 0.5)
print(eggs[0])
# 'hello'
print(eggs[1:3])
# (42, 0.5)
print(len(eggs))
# 3

print(type(('hello',)))
# <class 'tuple'>
print(type(('hello')))
# <class 'str'>
