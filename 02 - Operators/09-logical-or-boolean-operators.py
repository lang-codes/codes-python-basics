# HEAD
# Logical, Boolean Operators
# DESCRIPTION
# Describes how boolean operators are used
# RESOURCES
# 

# 'and', 'or', and 'not' keys are boolean operators
# works on boolean values or conditions returning booleans
#        and returns boolean values
# (condition) and (condition)
# (condition) or (condition)
# (not condition) and (condition)
# (boolean) and (boolean)
# (boolean) or (boolean)
# (not boolean) and (boolean)

name = "test"

# Different usages of 'not' key
# 'not' key is a checker that checks for inverse of result
#       of condition or boolean representation of a 
#       variable/value
# 'not' key returns a boolean value

# if (not name == "test"):
# if not type(name) == "str":
# if not (name == "test"):
# if (name != "test"):

# not checks for inverse of boolean value
# returns boolean
# 0, None, undefined is considered Falsy
# 1, presence, having value is considered Truthy
if not name:
    print(name, 4)

# 'is' checks for inverse of similarity in type
# returns boolean
if (type(name) is str):
    print(name, 1)

# 'and' checks for two boolean values 
#       or boolean values from conditions
# Presedence for 'and' key is False/Falsy Value
# (means returns False even if one condition has Falsy value)
# returns boolean
if (isinstance(name, str) and (not name)):
    print(name, 2)

# 'and' key will allow getting into the 
#           block only if both conditions return True
# 'and' key has precendence for Falsy value
# (means returns False even if one condition has Falsy value)
# returns boolean
if (isinstance(name, str) and (not name == 'test')):
    print(name, 2)

# 'or' key will allow getting into the 
#           block if either one returns True
# 'or' key has precendence for Truthy value 
# (means returns True even if one condition has Truthy value)
# returns boolean
if (isinstance(name, str) or (not name == 'test')):
    print(name, 2)

# Type Conversion blank string
typeConversion = bool("")
print("typeConversion", typeConversion)

# Type Conversion string
typeConversion = bool("I hate cybercrime")
print("typeConversion", typeConversion)
