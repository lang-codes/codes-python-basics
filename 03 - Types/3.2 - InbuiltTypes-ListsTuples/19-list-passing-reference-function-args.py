# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes how referencing works in lists
# RESOURCES
# 

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
# [0, 'Hello!', 2, 3, 4, 5]

print(cheese)
# [0, 'Hello!', 2, 3, 4, 5]

# Other example
def eggs(someParameter):
    someParameter.append('Hello')

someOtherParam = [1, 2, 3]
eggs(someOtherParam)
print('someOtherParam',someOtherParam)

