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

# 2
# # for item in range(int):
# #   execution block

# 3
# # for item in range(startInt, endInt):
# #   execution block


# # stepIncrement default is 1 in case of 
# #       above two use cases if not specified
# 4
# # for item in range(startInt, endInt, stepIncrement):
# #   execution block

# Variations of range() function:
# range(int)
# range(start, stop)
# range(start, stop, increment)


# # Range
# range(int) => no of iteration == range(0,10)
# range(start, end)
# range(start, end, step)

# for it in range(10):
#     print(it)

# # for(var i = 0, i<10; i++)
# for it in range(0, 10):
#     print(it)

# # # for(var i = 3, i<10; i++)
# # default increment == 1
# for it in range(3, 10):
#     print(it)



# for it in range(3, 10, 1):
#     print(it)


# for it in range(3, 10, 2):
#     print(it)
# # no context probably
# print(it)

# # for(var i = 0, i<5; i++)
# # default increment == 1
for i in range(5):
    print('range(5): Will print five times ' + str(i))

# # for(var i = 3, i<10; i++)
# # default increment == 1
for i in range(2, 6):
    print('range(2, 6): Will print six times using start and finish - will include 1st and exclude last ' + str(i))

# # for(var i = 3, i<10; i++)
for i in range(0, 6, 1):
    print('range(0, 6, 1): Will print two times using number of increments in the last ' + str(i))

# # for(var i = 3, i<10; i+2)
for i in range(0, 6, 2):
    print('range(0, 6, 2): Will print two times using number of increments in the last ' + str(i))

list = [2, 3, 4, 5, 6, 7, 8]

# using enumerate(iterator) function to get 
#       a tuple of (index, value) which can be destructured
for idx, item in enumerate(list):
    print("enumerate(list) usage", item, idx)

# Single line for expression statement to create lists
# STRUCTURE
# [expressionUsingValue for Value in list]

[print("Single line for loop [expressionUsingValue for Value in list]", i) for i in [2,3,4,5,6,7]]

# Single line for expression statement to create dictionaries
# STRUCTURE
# [expressionUsingValue for Value in list]

{ i:i for i in [2,3,4,5,6,7]}

