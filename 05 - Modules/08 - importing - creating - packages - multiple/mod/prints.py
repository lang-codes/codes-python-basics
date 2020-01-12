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


# Declaring the printer function
def printer():
    print('Print Module Called')


if __name__ == '__main__':
    printer()
    print("Triggered from __name__ == '__main__' of print")
