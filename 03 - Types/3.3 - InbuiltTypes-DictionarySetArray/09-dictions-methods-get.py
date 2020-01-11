# Describes the assigning, working, and method usages of dictionaries

# Using the get method in dictions
# obj.get('key', defaultValue)
# Returns the value of the key
# Default value avoids errors when the key is not present

obj = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(obj.get('cups', 0)) + ' cups.')
# 'I am bringing 2 cups.'
print('I am bringing ' + str(obj.get('coffeebeans', 0)) + ' coffeebeans.')
# 'I am bringing 0 coffeebeans.'
