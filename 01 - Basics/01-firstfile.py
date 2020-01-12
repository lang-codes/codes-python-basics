# HEAD
# Python Basics - Variable and common inbuilt functions
# DESCRIPTION
# Describes how to work with a file, some 
#       basic commonly used inbuilt functions
# 
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
# RESOURCES
# 


# This program says hello and asks for my name.
# myName and myAge are variables that hold some data

print('Hello world!')

# ask for their name - input
# input() function takes the values as a string
print('What is your name?') 
myName = input()

# printing myName
print('It is good to meet you, ' + myName)
print('The length of your name is:')

# printing length of myName
print(len(myName))

# ask for their age - input
print('What is your age?')    
myAge = input()

# printing myAge+1 below
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
