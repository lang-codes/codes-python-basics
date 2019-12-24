# Describes the inbuilt datatypes in python3

# INBUILT DATA TYPES
# https://stackoverflow.com/questions/1331471/in-memory-size-of-a-python-structure
# https://www.programiz.com/python-programming/variables-datatypes

import sys
import array as arr

name = "str"
age = 10
# Integers in Python 3 are of unlimited size.

# Python 2 has two integer types - int and long.
# # There is no 'long integer' in Python 3 anymore.
# Long function is in 2.x
# https://docs.python.org/2/library/functions.html
# Long is not there in 3.x
# https://docs.python.org/3/library/functions.html

# Conversion to long. Works with only python 2.x 
#       and not python3

# Function:: long(x, base=10)
# print(long(ages))

ages = 10.54
# Floats may also be in scientific notation,
# with E or e indicating the power of 10 
#       (2.5e2 = 2.5 x 10power2 = 250)

agess = 10.56j

# INBUILT TYPES
list = [1, 2, 3, 4, 5, 6]
tuples = ("w", "e", "t", "y")
sets = set([1, 2, 3, 4, 5, 6])
fsets = frozenset([1, 2, 3, 4, 5, 6])

# DATA TYPES
arrys = arr.array('d', [1, 2, 3, 4, 5, 6])

# http://deeplearning.net/software/theano/tutorial/python-memory-management.html
# Long was explained as Complex
#  It was not complex!! but long
# Complex numbers representation is for "Complex numbers"
# Complex numbers follow a + bJ,
# ** Both a and b are floats
# and J (or j) represents the square root of -1 
#       (which is an imaginary number).
# The real part of the number is a, and 
#       the imaginary part is b.
# Complex numbers are not used much in Python programming.

print("\nByte size of each of following:\n")

print("name:", name, "bytes", sys.getsizeof(name))
print("cint:", age, "bytes", sys.getsizeof(age))
print("ages:", ages, "bytes", sys.getsizeof(ages))
print("agess:", agess, "bytes", sys.getsizeof(agess))
print("list:", list, "bytes", sys.getsizeof(list))
print("tuples:", tuples, "bytes", sys.getsizeof(tuples))
print("sets:", sets, "bytes", sys.getsizeof(sets))
print("fsets:", fsets, "bytes", sys.getsizeof(fsets))
print("arrys:", arrys, "bytes", sys.getsizeof(arrys))
