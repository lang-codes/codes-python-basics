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

# Just defining what has to be exported using the __all__ variable
# Please remember the importing file can bypass this by 
#       explicitly accessing the unexported and unscoped file module
__all__ = ['print']

# To remove modules just remove the name of the module from the array of modules to be exported
# __all__ = []
