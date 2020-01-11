# Describes usage of while (conditions) statement

# The condition is checked everytime before 
#       iteration execution block starts
# Will keep iterating until the condition 
#       returns a Falsy value

# USAGE
# while (conditions):
#     execution block

name = ''
while (name == '' or name == 'aptech'):
    print('Enter a new name')
    name = input()
    print('Hello ' + str(name))
print('Finished loop')
