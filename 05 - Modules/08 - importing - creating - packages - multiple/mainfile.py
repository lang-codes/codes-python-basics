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


# Allowing import of all modules by allowing the namespace availability
# This will not import all the modules, they have to be imported specifically
from mod import *

# Explicit import of file modules
# from mod import inputs, prints

# This is a script file when yu run this file as the 
#       main python file importing other packages/modules
# The imported modules or packages will be give the directory name 
#       or the module's name the filename's name respectively depending 
#       on whether the __name__ takes default pythons naming or __name__ 
#       value provided by you.

if __name__ == "__main__":
    # Trying to access the following objects will throw object
    inputs.inputprinter()
    prints.printer()
