# HEAD
# Modules - Creating and using directory module as package
# DESCRIPTION
# Describes the usage of package init.py file with other file module
# Imports file module explicitly - bypasses __init__.py scoping
# Imports also uses alias for the imported file module
# Describes usage of import statements 
#       and using a directory + function as a package
# Creating __init__.py to create a package
# Describes the usage of this file as a 
#       module (not as a script file) using __name__
#       with default value provided by python as __main__,
#       which basically means its the main script file
# RESOURCES
# 


# Import traps
# http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html
# main module since no __name__ has been specified

from foo import *

def main():
    inputs.inputprinter()
    print.printer()
    print.inputprinter()

if __name__ == '__main__':
    main()
