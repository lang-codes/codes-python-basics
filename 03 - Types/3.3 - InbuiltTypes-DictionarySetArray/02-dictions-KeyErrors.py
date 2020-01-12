# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes the assigning, working, and method usages of dictionaries
#       .keys() - Error
# RESOURCES
# 

# Demostrates assigning a diction value which is a set of {key: value} pair
spam = {'name': 'Zophie', 'age': 7}

# Accessing an unavailable key raises error
print(spam['color']) # accessing unavailable key

# Traceback (most recent call last):
#   File "<pyshell#1>", line 1, in <module>
#     spam['color']
# KeyError: 'color'