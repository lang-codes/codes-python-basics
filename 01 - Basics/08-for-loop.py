# HEAD
# Python FlowControl - for loop
# DESCRIPTION
# Describes usage of for loop in different ways 
#       for different usages
# 
# for loop can iterate over sequence or sequence like objects
# range() is an inbuilt function that returns 
#       results over time during iteration
# range() returned a sequence in py2.x
# RESOURCES
# 


# # USAGE
# 1
# # for item in iterator:
# #   execution block
# # Based on total number of items in the list

ls = [2, 3, 4, 5, 6, 7, 8]

# using iterator to get 
#       a item which is iterated
for item in ls:
    print('for item in ls ' + str(item))

# Usage of enumerate() function:
# enumerate(list)
# using enumerate(iterator) function to get 
#       a tuple of (index, value) which can be destructured
for idx, item in enumerate(ls):
    print("enumerate(list) usage: for idx, item in enumerate(ls): ", item, idx)


# Variations of range() function:
# range(int)
# range(start, stop)
# range(start, stop, increment)


# 2
# # for item in range(int):
# #   execution block
# # Based on total iterations specified


# 3
# # for item in range(startInt, endInt):
# #   execution block
# # Based on total iterations specified


# # stepIncrement default is 1 in case of 
# #       above two use cases if not specified
# 4
# # for item in range(startInt, endInt, stepIncrement):
# #   execution block
# # Based on total iterations specified


# # for(var i = 0, i<5; i++)
# # default increment == 1
for i in range(5):
    print('range(5): Will print five times ' + str(i))

# # for(var i = 2, i<6; i++)
# # default increment == 1
for i in range(2, 6):
    print('range(2, 6): Will print six times using start and finish - will include 1st and exclude last ' + str(i))

# # for(var i = 0, i<6; i++)
for i in range(0, 6, 1):
    print('range(0, 6, 1): Will print two times using number of increments in the last ' + str(i))

# # for(var i = 0, i<6; i+2)
for i in range(0, 6, 2):
    print('range(0, 6, 2): Will print two times using number of increments in the last ' + str(i))


# Single line for expression statement to create lists
# STRUCTURE
# [expressionUsingValue for Value in list]

[print("Single line for loop [expressionUsingValue for Value in list]", i) for i in [2,3,4,5,6,7]]


# Single line for expression statement to create dictionaries
# STRUCTURE
# {Value:Value for Value in list}

diction = { i:i for i in [2,3,4,5,6,7]}
print(diction)

