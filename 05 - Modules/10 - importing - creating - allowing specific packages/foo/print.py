# HEAD
# Modules - Creating and using directory module as package
# DESCRIPTION
# Describes the usage of package init.py file with other file module
# Imports file module explicitly - bypasses __init__.py scoping
# Imports also uses alias for the imported file module
# Describes usage of import statements 
#       and using a directory + function as a package
# Creating __init__.py to create a package
# RESOURCES
# 

# print file module
# since it is imported into another file the __name__ is
#       assigned with the filename or directory module
#       or package name as __name__ value


def printer():
    print('Print Module Called')

def inputprinter():
    print('Enter your name:')
    strs = input()
    print(str(strs))