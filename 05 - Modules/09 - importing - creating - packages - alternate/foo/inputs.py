# HEAD
# Modules - Creating and using directory module as package
# DESCRIPTION
# Describes the usage of package init.py file with other file module
# Describes usage of import statements 
#       and using a directory + function as a package
# Creating __init__.py to create a package
# Describes the usage of this file as a 
#       module (not as a script file) using __name__
#       with default value provided by python as __main__,
#       which basically means its the main script file
# RESOURCES
# 

__name__ = "customname"

def inputprinter():
    print('Enter your name:')
    strs = input()
    print(str(strs))

if __name__ == '__main__':
    # Remember the console will wait for your input
    inputprinter()
    print("Triggered from __name__ == '__main__' of print")
elif __name__ == "customname":
    inputprinter()
    print("Triggered from __name__ == 'customname' of print")

