# COMPLEX NUMBERS
# https://en.m.wikipedia.org/wiki/Complex_number
# Usage and behaviour in python codes
# Complex numbers end with a 'j' key in the 
#       end of the integer/float
# Inbuilt function complex() creates a complex number

# USAGE
# complex(real, imag)
# You can add two complex numbers but 
#       there will be representation
#       when a normal number and complex number is added

cmplx0 = 1.23456789j
print(0, cmplx0, cmplx0.real, cmplx0.imag)
cmplx1 = 2 + 1.23456789j
print(1, cmplx1, cmplx1.real, cmplx1.imag)
cmplx2 = 1.23456789j + 2.345678901
print(2, cmplx2, cmplx2.real, cmplx2.imag)
cmplx3 = 1.23456789j + 2.345678901j
print(3, cmplx3, cmplx3.real, cmplx3.imag)

# complex(real, imag)
cmplx4 = complex(1.23456789)
print(4, cmplx4, cmplx4.real, cmplx4.imag)
cmplx5 = complex(0, 1.23456789)
print(5, cmplx5, cmplx5.real, cmplx5.imag)
cmplx6 = complex(1.23456789, 0)
print(6, cmplx6, cmplx6.real, cmplx6.imag)
cmplx7 = complex(2, 1.23456789)
print(7, cmplx7, cmplx7.real, cmplx7.imag)
cmplx8 = complex(1.23456789, 2)
print(8, cmplx8, cmplx8.real, cmplx8.imag)
