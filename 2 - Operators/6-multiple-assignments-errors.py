# Describe incorrect usage of 
#       multiple assignation which throws error

# The number of items in the destructuring 
#       have to be the same as variables used for assignation
cat = ['fat', 'orange', 'loud']

# Will give an error since size is different
size, color, disposition, name = cat

# ERROR DETAILS -
# Traceback (most recent call last):
#   File "<pyshell#84>", line 1, in <module>
# size, color, disposition, name = cat
# ValueError: need more than 3 values to unpack
