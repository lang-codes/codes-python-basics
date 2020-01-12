# HEAD
# Modules - Creating Modules and Using __init__.py
# DESCRIPTION
# Describes the usage of the file as a module (not as a script file)
# Using __init__.py and scoping 
#       file modules inside a module
# Exports prints.py and inputs.py using __input__.py
# RESOURCES
# 

# Declaring the printer function
def printer():
    print('Print Module Called')


if __name__ == '__main__':
    printer()
    print("Triggered from __name__ == '__main__' of print")

