# Describes how multiple assignment works

# Works on sequences(lists/tuples), etc
# The number of variables have to be "same" as number of items
# This is referred to as destructuring
# Destructuring also applies to function 
#           multiple return values which return tuple


cat = ['fat', 'orange', 'loud']
# Applying destructuring
# destructring can be applied to all sequences and dictionaries
size, color, disposition = cat


# Multiple return values from function
# returns the values as tuples
def helloMultiple(name):
    print('Howdy! ' + name)
    return 'name', name


# Applying destructuring to return tuple
# returns the values as tuples which can be destructured
# destructring can be applied to all sequences and dictionaries
var1, var2 = helloMultiple(
    'Testing Multiple returns captured in multiple values')
print(var1, var2)
