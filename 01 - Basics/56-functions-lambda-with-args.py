# HEAD
# Python 
# DESCRIPTION
# Describes how 
#       - lambda functions are created using arguments
# 
# RESOURCES
# 

# Passing single args to Lambda functions with return statements
lbd = lambda x: x
print(lbd(2))

# Passing multiple args to Lambda functions with return statements
lbd = lambda x, y: x, y
print(lbd(2, 3))

# Passing single or multiple args to Lambda functions with no return but execution statements
lbd = lambda x, y: print(x, y)
lbd(2, 3)
