# Describes the assigning, working, and method usages of dictionaries

obj = {'color': 'red', 'age': 42}

# Using multiple assignments from the item tuple returned during each iteration 
for k, v in obj.items():
    print('Key: ' + k + ' Value: ' + str(v))

# Using multiple assignments from the item tuple returned during each iteration
# Looping through key:value of the dictions
for k, v in obj.items():
        print('Key:Value', k, v)
