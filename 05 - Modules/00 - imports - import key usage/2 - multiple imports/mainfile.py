# Describes the suage of package init.py file along with other module

# Allowing import of all modules by allowing the namespace availability
# This will not import all the modules, they have to be imported specifically
from mod import *

# Explicit import of file modules
# from mod import inputs, prints

# Trying to access the following objects will throw object
inputs.inputprinter()
prints.printer()
