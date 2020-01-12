# HEAD
# Modules - Creating and using directory module as package
# DESCRIPTION
# Describes usage of import statements 
#       and using a directory + function as a package
# Creating __init__.py to create a package
# RESOURCES
# 


# Import traps
# http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html
# main module since no __name__ has been specified

from foo.print import *

def main():
    printer()
    inputprinter()

if __name__ == '__main__':
    main()