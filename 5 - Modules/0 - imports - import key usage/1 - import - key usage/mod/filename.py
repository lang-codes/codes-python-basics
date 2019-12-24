# Describes usage of import statements and using a file as a import

# Describes what is a main module
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do

# We are creating a module named print below
# print module

# By uncommenting the following line `__name__ = "print"` you invariably assign the
#       variable __name__ as "print" and due to which the if statement will not execute
# If you dont uncomment the following line then default value to the value __name__ will be "__main__"
#       This is handy since python will allow you to run this file as a script
#       However, if __name__ is not specified and the file is imported into another file
#       for usage of functions then again the if __name__ == will not be executed

# __name__ = "print"

print("First statement")

def printer():
    print('Print Module Called')

print("Second statement")

def inputprinter():
    print('Enter your name:')
    strs = input()
    print(str(strs))

print("Third statement")

# The following if statement runs if this file is directly executed
#       and __name__ = "print" is commented
# Will run since this file will assign default value will then be __main__
# This following code will not be executed if the file is imported by other files
if __name__ == '__main__':
    printer()
    # Remember the console will wait for your input
    inputprinter()
    print("Triggered from __name__ == '__main__' of print")

print("Fourth statement")

# The following if statement runs if this file is directly executed
#       and __name__ = "print" is not commented
# This following code will be executed if the file is imported by other files
#       and will result in errors
if __name__ == 'print':
    printer()
    inputprinter()
    print("Triggered from __name__ == 'print' of print")

print("Fifth statement")
