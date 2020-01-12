# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes using loops on list
# RESOURCES
# 

catNames = []

# Following is an infinite while loop
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    # list concatenation
    catNames = catNames + [name]
print('The cat names are:')

# Following is an for loop list
for name in catNames:
    print('  ' + name)

# looping list and working with list and loops
