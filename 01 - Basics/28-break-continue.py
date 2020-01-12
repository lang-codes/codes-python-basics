# HEAD
# Using `continue` and `break` keys
# DESCRIPTION
# Describes usage of 'continue' and 'break' keys
# 'continue' key skips execution of block 
#       below it and continues to next
#       logical step after the continue statement
# 'break' key will break out of the loop completely; 
#       without further iteration
#  PENDING: continue usage with functions to exit program
# RESOURCES
# 

for i in range(0, 6, 1):
    if i == 3:
        # Will skip execution of following 
        #       codes of this iteration
        # and continue to next iteration
        continue
    print('Will print two times using number of increments in the last ' + str(i))

for i in range(0, 6, 1):
    if i == 3:
        # Will break out of the loop
        break
    print('Will print two times using number of increments in the last ' + str(i))
