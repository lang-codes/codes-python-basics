# HEAD
# Python FlowControl - for loop
# DESCRIPTION
# Describes usage of for loop in different ways
#       for different usages
#
# 'for' loop can iterate over iterable (sequence like) or sequence objects
# Result provided during every loop is an item
# 
# RESOURCES
#


# # USAGE
# 1
# # for item in iterator:
# #   execution block
# # Based on total number of items in the list

ls = [2, 3, 4, 5, 6, 7, 8]


# Using iterator to get
#       a item which is iterated
for item in ls:
    print('for item in ls ' + str(item))
