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
# This is the main module since no 
#       __name__ has been specified for this file

from foo import print as p

# OTHER IMPORT METHODS

# # Following allows access of print file module directly without alias
# # Access function to be used as print.printer()
# from foo import print

# # Following allows access of printer function directly
# # Access function to be used as printer()
# from foo.print import printer

# # Following allows access of inputprinter function directly
# # Access function to be used as inputprinter()
# from foo.print import inputprinter

# # Following allows access of inputprinter function with an alias inpr
# # Access function to be used as inpr()
# from foo.print import inputprinter as inpr

# # Following allows access of all functions directly
# # Access function to be used as printer() and inputprinter()
# from foo.print import *

def main():
    print(print.__name__)
    p.printer()
    p.inputprinter()

if __name__ == '__main__':
    main()
