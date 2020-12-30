# HEAD
# Python FlowControl - for loop
# DESCRIPTION
# Describes usage of for loop in different ways
#       for different usages
#
# 'for' loop can iterate over iterable (sequence like) or sequence objects
# Result provided during every loop is an index and the relative item
# 
# RESOURCES
# 


# # USAGE
# 1
# # for item in iterator:
# #     execution block
# # Based on total number of items in the list

ls = [2, 3, 4, 5, 6, 7, 8]


# Using iterator to get
#       a item which is iterated
for item in ls:
    print("Provides item of the iterator")
    print('for item in ls ' + str(item))


# Usage of enumerate() function:
# enumerate(list)
# using enumerate(iterator) function to get
#       a tuple of (index, value) which can be destructured
for item in enumerate(ls):
    print("Provides index and its item of the iterator")
    print("enumerate(list) usage: for item with first item as idx& second as item in enumerate(ls): ", item[0], item[1])


for idx, item in enumerate(ls):
    print("Provides index and its item of the iterator")
    print("enumerate(list) usage: for idx, item in enumerate(ls): ", idx, item)

