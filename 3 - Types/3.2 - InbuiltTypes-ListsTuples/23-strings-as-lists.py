# Describes how strings behave as a list or a sequence
# Strings can be referenced per character using indexes like lists
# String indexing also starts from 0/Zero
# Strings can be looped like lists

name = 'Zophie'
print(name[0])
# 'Z'
print(name[-2])
# 'i'
print(name[0:4])
# 'Zoph'
print('Zo' in name)
# True
print('z' in name)
# False
print('p' not in name)
# False
for i in name:
    print('* * * ' + i + ' * * *')
