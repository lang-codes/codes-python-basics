# HEAD
# DataType - Dictionaries Getting True Lists from 
#       methods like .keys(), .values(), .items()
# DESCRIPTION
# Describes the assigning, working, and method usages of dictionaries
# RESOURCES
# 

obj = {'color': 'red', 'age': 42}

# Printing the keys list
print('keys', obj.keys())

# THe methods keys(), items(), values() return true lists
# dict_keys(['color', 'age'])
list(obj.keys())
# ['color', 'age']
