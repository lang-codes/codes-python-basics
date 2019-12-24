# Describes the assigning, working, and method usages of dictionaries

# String variable
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

# Creating a empty diction
obj = {}

# Adding default keys and values
for keyitem in message:
    obj.setdefault(keyitem, 0)
    obj[keyitem] = obj[keyitem] + 1

# Print object
print(obj)
