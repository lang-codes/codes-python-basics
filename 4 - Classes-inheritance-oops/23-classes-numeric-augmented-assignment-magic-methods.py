# Describes the magic methods of classes
# https://rszalski.github.io/magicmethods/

# Augmented assignment

# Python also has a wide variety of magic methods to allow custom behavior to be defined for augmented assignment. You're probably already familiar with augmented assignment, it combines "normal" operators with assignment. If you still don't know what I'm talking about, here's an example:

# x = 5
# x += 1 # in other words x = x + 1

# Each of these methods should return the value that the variable on the left hand side should be assigned to (for instance, for a += b, __iadd__ might return a + b, which would be assigned to a). Here's the list:

# __iadd__(self, other)
#     Implements addition with assignment.
# __isub__(self, other)
#     Implements subtraction with assignment.
# __imul__(self, other)
#     Implements multiplication with assignment.
# __ifloordiv__(self, other)
#     Implements integer division with assignment using the //= operator.
# __idiv__(self, other)
#     Implements division with assignment using the /= operator.
# __itruediv__(self, other)
#     Implements true division with assignment. Note that this only works when from __future__ import division is in effect.
# __imod__(self, other)
#     Implements modulo with assignment using the %= operator.
# __ipow__
#     Implements behavior for exponents with assignment using the **= operator.
# __ilshift__(self, other)
#     Implements left bitwise shift with assignment using the <<= operator.
# __irshift__(self, other)
#     Implements right bitwise shift with assignment using the >>= operator.
# __iand__(self, other)
#     Implements bitwise and with assignment using the &= operator.
# __ior__(self, other)
#     Implements bitwise or with assignment using the |= operator.
# __ixor__(self, other)
#     Implements bitwise xor with assignment using the ^= operator.
