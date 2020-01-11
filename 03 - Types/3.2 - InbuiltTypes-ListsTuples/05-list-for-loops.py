# Describes using loops on lists

# Using for loops to iterate over the items
# allows access of items in list
for item in [20, 21, 22, 23]:
    print(item)

# allows access of index, items in list
for idx, item in [20, 21, 22, 23]:
    print(idx, item)

# Using for loops to iterate based on length of list
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

# allows use of index inside for loop
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
