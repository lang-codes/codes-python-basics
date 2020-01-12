# HEAD
# DataType - Array Creation and usage
# DESCRIPTION
# Describes the assigning, working usages 
#       of Arrays using inubilt Library
# RESOURCES
# 

# Importing Array module (all exports)
from array import *


# Alternate import statement
# import array
# import array as array

# arrame = array(typecode, [Initializers])
arr = array('L',[100000,2,3,4])
print(arr)

# ‘b’ -> Represents signed integer of size 1 byte
# ‘B’ -> Represents unsigned integer of size 1 byte
# ‘c’ -> Represents character of size 1 byte
# ‘u’ -> Represents unicode character of size 2 bytes
# ‘h’ -> Represents signed integer of size 2 bytes
# ‘H’ -> Represents unsigned integer of size 2 bytes
# ‘i’ -> Represents signed integer of size 2 bytes
# ‘I’ -> Represents unsigned integer of size 2 bytes
# ‘w’ -> Represents unicode character of size 4 bytes
# ‘l’ -> Represents signed integer of size 4 bytes
# ‘L’ -> Represents unsigned integer of size 4 bytes
# ‘f’ -> Represents floating point of size 4 bytes
# ‘d’ -> Represents floating point of size 8 bytes

