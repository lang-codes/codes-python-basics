# HEAD
# Python FlowControl - for loop
# DESCRIPTION
# Describes overload (multiway invocation) usage of for loop in different ways
#       for different usages
#
# Result provided during every loop is an index like item (numerical series)
# range() is an inbuilt function that returns
#       results over time during iteration
# range() returned a sequence in py2.x
# 
# RESOURCES
#


# Overload (multiway invocation) Variations of range() function:
#   range(int)
#   range(start, stop)
#   range(start, stop, increment)


# 2
# # for item in range(int):
# #   execution block
# # Based on total iterations specified


# # USAGE SIMILAR TO - for(var i = 0, i<5; i++)
# # default increment == 1
for i in range(5):
    print('range(5): Will print five times ' + str(i))


# 3
# # for item in range(startInt, endInt):
# #   execution block
# # Based on total iterations specified

# # USAGE SIMILAR TO -  for(var i = 2, i<6; i++)
# # default increment == 1
for i in range(2, 6):
    print('range(2, 6): Will print six times using start and finish - will include 1st and exclude last ' + str(i))


# # stepIncrement default is 1 in case of
# #       above two use cases if not specified
# 4
# # for item in range(startInt, endInt, stepIncrement):
# #   execution block
# # Based on total iterations specified


# # USAGE SIMILAR TO - for(var i = 0, i<6; i++)
# # increment implementation is 1
for i in range(0, 6, 1):
    print('range(0, 6, 1): Will print two times using number of increments in the last ' + str(i))


# # USAGE SIMILAR TO - for(var i = 0, i<6; i+2)
# # increment implementation is 2
for i in range(0, 6, 2):
    print('range(0, 6, 2): Will print two times using number of increments in the last ' + str(i))
