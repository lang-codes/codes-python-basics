# HEAD
# Python Basics - while infinite loops
# DESCRIPTION
# Describes usage of while (and conditions) loop statements while are infinite
#
# Since the condition is always true,
#       the loop below is infinite loop
#
# A condition that returns always True is an infinite loop
# A condition can also be replaced by a boolean
#       while True:
#           # infinite loop
#       while False:
#           # no iteration loop
#
# RESOURCES
#

# Defining a name with blank string
name = ''

# Following loop is always infinite
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

