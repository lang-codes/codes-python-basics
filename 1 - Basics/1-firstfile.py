# Describe how to write a first program

# input() is a inbuilt function that takes input from user 
#       in the command line
# print() is a inbuilt function that takes a 
#       value or variable and prints string representation 
#       in the command line
# str() is a inbuilt function that takes a 
#       value and gives string representation of the value
# int()  is a inbuilt function that takes a 
#       number like character and converts to a integer
# semi-colon to end the logical line is optional 
#       but can be used
# Variables do not have types description 
#       like in typed languages

# This program says hello and asks for my name.
# myName and myAge are variables that hold some data

print('Hello world!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
