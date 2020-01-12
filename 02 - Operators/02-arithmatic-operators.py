# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes all the operators related to arithmatic
# RESOURCES
# 

# Different operators are available for 
# + , - , * , / , %, //

# Addition Operator
add = 1 + 2 
# Result > 3
print('add:', add)

addStrings = "stringone" + "string2"
# Result > "stringonestring2"
print('addStrings:', addStrings)

# addNumAndString = 1 + "string"
# # Result > Error due to different data types 
# print('addNumAndString:', addNumAndString)

# Negative Operator
sub = 2 - 1
# Result > 1
print('sub:', sub)

# Multiplication Operator
mul = 2 * 1
# Result > 2
print('mul:', mul)

# Division Operator
div = 2/1
# Result > 2
print('div:', div)

# Modulus Operator - Remainder
mod = 10%2
# Result > 0
print('mod:', mod)

# Modulus Operator - Quotient
quo = 10//2
# Result > 5
print('quo:', quo)

# Precedence of operators
# / , * , - , +

# Using operators for string
strjoin = "Test" + " and Tester"
print('strjoin:', strjoin)


# Truthy value takes 1 as interger and Falsy as 0
# Adding two boolean Truthy Values
boolAdd = True + True
print("boolAdd", boolAdd)

# Adding two boolean Truthy and Falsy Values
boolAdd = True + False
print("boolAdd", boolAdd)

# Adding two boolean Truthy and Numeric Values
boolNumAdd = True + 2
print("boolNumAdd", boolNumAdd)

# Muliplying two boolean Truthy and Numeric Values
boolMul = True * 2
print("boolMul", boolMul)

