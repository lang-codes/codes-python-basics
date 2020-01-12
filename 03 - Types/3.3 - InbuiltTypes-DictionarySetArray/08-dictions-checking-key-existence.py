# HEAD
# DataType - Dictionaries key existence
# Getting True Lists from 
#       methods like .keys(), .values(), .items()
# DESCRIPTION
# Describes the assigning, working, and method usages of dictionaries
# RESOURCES
# 

obj = {'name': 'Zophie', 'age': 7}

# Checking item present in the list returned by functions
print('name' in obj.keys())
# True
print('Zophie' in obj.values())
# True
print('color' not in obj.keys())
# True
print('color' not in obj.keys())
# True

# Variation in usage of keys using the diction directly
# 'color' in obj is essentially a shorter version of writing 'color' in obj.keys()
print('color' in obj)
# False
