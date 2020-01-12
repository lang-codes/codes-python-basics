# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes the magic methods of classes
# RESOURCES
# 
# https://rszalski.github.io/magicmethods/

# Reflected arithmetic operators

# You know how I said I would get to reflected arithmetic in a bit? Some of you might think it's some big, scary, foreign concept. It's actually quite simple. Here's an example:

# some_object + other

# That was "normal" addition. The reflected equivalent is the same thing, except with the operands switched around:

# other + some_object

# So, all of these magic methods do the same thing as their normal equivalents, except the perform the operation with other as the first operand and self as the second, rather than the other way around. In most cases, the result of a reflected operation is the same as its normal equivalent, so you may just end up defining __radd__ as calling __add__ and so on. Note that the object on the left hand side of the operator (other in the example) must not define (or return NotImplemented) for its definition of the non-reflected version of an operation. For instance, in the example, some_object.__radd__ will only be called if other does not define __add__.

# __radd__(self, other)
#     Implements reflected addition.
# __rsub__(self, other)
#     Implements reflected subtraction.
# __rmul__(self, other)
#     Implements reflected multiplication.
# __rfloordiv__(self, other)
#     Implements reflected integer division using the // operator.
# __rdiv__(self, other)
#     Implements reflected division using the / operator.
# __rtruediv__(self, other)
#     Implements reflected true division. Note that this only works when from __future__ import division is in effect.
# __rmod__(self, other)
#     Implements reflected modulo using the % operator.
# __rdivmod__(self, other)
#     Implements behavior for long division using the divmod() built in function, when divmod(other, self) is called.
# __rpow__
#     Implements behavior for reflected exponents using the ** operator.
# __rlshift__(self, other)
#     Implements reflected left bitwise shift using the << operator.
# __rrshift__(self, other)
#     Implements reflected right bitwise shift using the >> operator.
# __rand__(self, other)
#     Implements reflected bitwise and using the & operator.
# __ror__(self, other)
#     Implements reflected bitwise or using the | operator.
# __rxor__(self, other)
#     Implements reflected bitwise xor using the ^ operator.

