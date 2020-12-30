# HEAD
# NESTED LAMBDA FUNCTIONS 
# DESCRIPTION
# Describes how 
#       - to create nested lambdas
# 
# RESOURCES
# 


# STORING NESTED FUNCTIONS IN VARIABLES

# lambda allows nesting inside lambdas without arguments
action = lambda x: lambda: x
ans = action(99)
print(ans())


# lambda allows nesting inside lambdas with arguments
action = lambda x: lambda newx: x + newx
ans = action(99)
print(ans(1))

