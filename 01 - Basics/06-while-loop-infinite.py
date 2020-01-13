# HEAD
# Python FlowControl - while loops
# DESCRIPTION
# Describes usage of while (and conditions) loop statements
# 
# Since the condition is always true, 
#       the loop below is infinite loop
# 
# Declaring a 'while' loop with one condition
# The loop will keep iterating till the 
#       value of name is not 'your name'. This may
#       become a infinite loop if the user does not 
#       enter the value 'your name'
# RESOURCES
# 


# Defining a name with blank string
name = ''


while name != 'your name':
    print('Enter your name.')
    # Getting a new string value for name
    name = input()
print('Thank you!')

# Following is an loop that
#       never does even one iteration
while True:
    print("I am infinite loop")

# Following is an infinite loop that
#       that prints until you stop the process
while True:
    print("I am infinite loop")
