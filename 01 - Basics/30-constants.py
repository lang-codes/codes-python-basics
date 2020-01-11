# Describes constants in python

# Constants are declared in python in a different module
# Concept of constants dont exists in python
# Generally represented in capitals

PI_ = 3.14
print("PI_", PI_)
# Following can be modified, so concept of constants dont apply
PI_ = 3.15
print("PI_ Changed", PI_)

# Alternatively, a scope variable can be used
# SINGLE CONSTANT


def PI():
    PI = 3.14
    return PI


# PI as a constant resulting from function invocation
# The function PI is always a constant
# _PI, however, can be changed
print("PI()", PI())
_PI = PI()

# Changing _PI works but PI() remains same
_PI = 3.15
print("_PI Changed", _PI)
print("PI()", PI())

# MAP OF CONSTANTS
# ALLCONSTANTS as a constant map resulting from function invocation
# The function ALLCONSTANTS always returns a constant
# _ALLCONSTANTS, however, can be changed


def ALLCONSTANTS():
    PI = 3.14
    GRAVITY = 9.8
    return {"PI": PI, "GRAVITY": GRAVITY}


_ALLCONSTANTS = ALLCONSTANTS()
print("ALLCONSTANTS()", ALLCONSTANTS())
print("_ALLCONSTANTS['PI']", _ALLCONSTANTS["PI"])
print("_ALLCONSTANTS['GRAVITY']", _ALLCONSTANTS["GRAVITY"])

# Changing _ALLCONSTANTS["PI"] or _ALLCONSTANTS["GRAVITY"] works
# but ALLCONSTANTS() remains same
_ALLCONSTANTS["PI"] = 3.15
_ALLCONSTANTS["GRAVITY"] = 9.9
print("ALLCONSTANTS()", ALLCONSTANTS())
print('_ALLCONSTANTS["PI"] Changed', _ALLCONSTANTS["PI"])
print('_ALLCONSTANTS["GRAVITY"] Changed', _ALLCONSTANTS["GRAVITY"])

# Alternatively, create a file module with variables referenced as CONSTANTS
# constants as a constant unchangable values resulting from different modules
# The function constants always returns a constant
import constants
print('constants.PI', constants.PI)
print('constants.GRAVITY', constants.GRAVITY)

# constants when applied to variable, however, can be changed
# The module values remain the same
GRAVITY = constants.GRAVITY
GRAVITY = 9.9
print('GRAVITY Changed', GRAVITY)
print('constants.GRAVITY', constants.GRAVITY)
