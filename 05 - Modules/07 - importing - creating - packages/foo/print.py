# HEAD
# Modules - Creating and using directory module as package
# DESCRIPTION
# Describes usage of import statements 
#       and using a directory + function as a package
# Creating __init__.py to create a package
# RESOURCES
# 


# print module
# since it is imported into another file the __name__ is
#       assigned with the filename as __name__ value


def printer():
    print('Print Module Called')

def inputprinter():
    print('Enter your name:')
    strs = input()
    print(str(strs))