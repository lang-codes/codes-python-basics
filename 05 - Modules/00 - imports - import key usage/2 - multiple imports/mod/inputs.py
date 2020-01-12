# HEAD
# Modules - Creating Modules and Using __init__.py
# DESCRIPTION
# Describes the usage of the file as a module (not as a script file)
# Using __init__.py and scoping 
#       file modules inside a module
# Exports prints.py and inputs.py using __input__.py
# RESOURCES
# 


# Declaring the inputprinter function
def inputprinter():
    print('Enter your name:')
    strs = input()
    print(str(strs))

if __name__ == '__main__':
    # Remember the console will wait for your input
    inputprinter()
    print("Triggered from __name__ == '__main__' of print")

