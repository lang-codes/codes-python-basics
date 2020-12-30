# HEAD
# Using `continue` and `break` keys
# DESCRIPTION
# Describes usage of 'break' keys
# 'break' key will break out of the loop completely; 
#       without further iteration
# 
# RESOURCES
# 


for i in range(0, 6, 1):
    if i == 3:
        # Will break out of the loop
        break
    print('Will print two times using number of increments in the last ' + str(i))



