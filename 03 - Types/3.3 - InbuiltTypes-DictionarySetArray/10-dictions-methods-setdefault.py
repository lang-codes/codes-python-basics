# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes the assigning, working, and method usages of dictionaries
# RESOURCES
# 

obj = {'name': 'Ganesh', 'age': 5}

# Add a key value pair
if 'color' not in obj:
    obj['color'] = 'light-brown'

print(obj)

obj = {'name': 'Ganesh', 'age': 5}

# Using setdefault function
obj.setdefault('color', 'light-brown')
# 'light-brown'

print(obj)
# {'color': 'light-brown', 'age': 5, 'name': 'Ganesh'}

obj.setdefault('color', 'white')
# 'light-brown'

print(obj)
