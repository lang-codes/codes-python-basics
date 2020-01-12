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

# inputs file module
# since it is imported into another file the __name__ is
#       assigned with the filename or directory module
#       or package name as __name__ value

def inputprinter():
    print('Enter your name:')
    strs = input()
    print(str(strs))

if __name__ == '__main__':
    # Remember the console will wait for your input
    inputprinter()
    print("Triggered from __name__ == '__main__' of print")

