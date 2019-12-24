# Describes typeconversion methods available in python

# These function can also be used to declare specific types
# When appropriate object is used, these functions can be
#       used to convert one type to another
#       Example: list <-> tuple
#       Example: list <-> str
#       Example: dict <-> sequence of key value tuples
# Other functions also exist like
#       list(), dict(), tuple(), set(), frozenset(), etc
# repr() function and str() function both provide 
#       the string representation of variable value
# As per documetation repr() provides more 
#       precise representation than str()

import sys

# STRING TYPE CONVERSION

# str() converts to string
sStr1 = str("Testing String")
print('str1', sStr1)
sStr2 = str(12)
print('str2', sStr2)
sStr3 = str(1.2345678901234567890)
print('str3', sStr3)

# repr() gives more precision while conversion to string
sRepr1 = repr("Testing String")
print('repr1', sRepr1)
sRepr2 = repr(12)
print('repr2', sRepr2)
sRepr3 = repr(1.2345678901234567890)
print('repr3', sRepr3)

# NUMBER TYPE CONVERSION AND MEMORY USAGE

# Type int(x) to convert x to a plain integer
cint = int(1.12345678901234567890)
print(cint)

# Type long(x) to convert x to a long integer - Python 2
# clong = long(1.12345678901234567890)
# print(clong)

# Type float(x) to convert x to a floating-point number.
cfloat = float(1.12345678901234567890)
print(cfloat)

# Type complex(x) to convert x to a complex number with real part x and imaginary part zero.
# Type complex(x, y) to convert x and y to a complex number with real part x and imaginary part y.
# x and y are numeric expressions
ccomplex = complex(1.12345678901234567890)
print(ccomplex)
# (1.1234567890123457+0j)

ccomplexs = complex(1, 1.12345678901234567890)
print(ccomplexs)
# (1+1.1234567890123457j)

print("\nByte size of each of following:\n")

print("cint:", cint, "bytes", sys.getsizeof(cint))
# print("clong:", clong, "bytes", sys.getsizeof(clong))
print("cfloat:", cfloat, "bytes", sys.getsizeof(cfloat))
print("ccomplex:", ccomplex, "bytes", sys.getsizeof(ccomplex))
print("ccomplexs:", ccomplexs, "bytes", sys.getsizeof(ccomplexs))
