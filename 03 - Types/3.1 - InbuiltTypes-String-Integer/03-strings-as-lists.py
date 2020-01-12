# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes how strings behave as a list or a sequence
# RESOURCES
# 


# Strings can be referenced per character using indexes like lists
# String indexing also starts from 0/Zero
# Strings can be looped like lists

name = 'Zophie'
# Reference using index of string character position
print(name[0])
# 'Z'

# Accessing the index using the negative number (access from the last)
print(name[-2])
# 'i'

# Access string characters as a subset using a range
# string[start:end]
# If start or end is not specified it is taken as the o or the last respectively
print(name[0:4])
# 'Zoph'

# Work with string for searching items in the list
print('Zo' in name)
# True
print('z' in name)
# False

# Work with string for searching items not in the list
print('p' not in name)
# False

# Loop through string loops
for i in name:
    print('* * * ' + i + ' * * *')
