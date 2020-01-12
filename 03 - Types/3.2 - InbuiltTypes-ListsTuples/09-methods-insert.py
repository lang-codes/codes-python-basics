# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes the insert method of lists
# RESOURCES
# 

# USAGE
# .insert(index, item)
# inserts an item in place of index in the list
# self modification function

lists = ['cat', 'dog', 'bat']
lists.insert(1, 'chicken')
print(lists)
lists.insert(-1, 'testsecondlastend')
print(lists)
lists.insert(len(lists), 'testend')
print(lists)
