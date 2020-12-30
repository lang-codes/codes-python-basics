# HEAD
# Python FlowControl - for loop
# DESCRIPTION
# Describes usage of for loop in different ways
#       for different usages
#
# Result provided during every loop is an item
# The resultant object is based on usage
# 
# RESOURCES
#


# Single line for expression statement to create lists
# STRUCTURE
# [expressionUsingValue for Value in list]

[print("Single line for loop [expressionUsingValue for Value in list]", i)
 for i in [2, 3, 4, 5, 6, 7]]


# Single line for expression statement to create dictionaries
# STRUCTURE
# {Value:Value for Value in list}

diction = {i: i for i in [2, 3, 4, 5, 6, 7]}
print(diction)
