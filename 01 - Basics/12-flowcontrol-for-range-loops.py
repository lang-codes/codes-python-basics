# HEAD
# Python FlowControl - for loop
# DESCRIPTION
# Describes usage of for loop in different ways 
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


# # Implements a range of index iterators creation 
# #         with ending value (end)
# #         default start == 0
# #         default increment == 1
for i in range(5):
    print('range(5): Will print five times ' + str(i))


# # Implements a range of index iterators creation 
# #         with starting and ending values (start, end)
# #         default increment == 1
for i in range(2, 6):
    print('range(2, 6): Will print six times using start and finish - will include 1st and exclude last ' + str(i))

