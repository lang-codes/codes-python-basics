# HEAD
# STORING LAMBDA FUNCTIONS
# DESCRIPTION
# Describes how 
#       - lambda functions are stored in variables, lists, tuples, dictionary
# 
# RESOURCES
# 


# STORING LAMBDA FUNCTIONS

# Storing Lambda functions in variables
lamb = lambda (x): x ** 3

print(lamb(5))


# STORING LAMBDA FUNCTIONS in lists or tuples or dictionaries

# Storing lambdas in lists
# 
# Allows us to embed a function within the code
# For instance, callback handlers are frequently coded as
#       inline lambda expressions embedded directly 
#       in a registration call's arguments list
L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

for f in L:
    print(f(3))

# Storing lambda in tuples
action = (lambda x: x,)
ans = action[0](99)
print(ans)

# Storing lambda in tuples
action = (lambda x: x, lambda y: print(y))
ans = action[0](99)
print(ans)
action[1](99)


# STORING ENCLOSED NESTED FUNCTIONS IN VARIABLES

# lambda also has access to the names in any enclosing lambda
action = (lambda x: (lambda newx: x + newx))
ans = action(99)
print(ans(1))

