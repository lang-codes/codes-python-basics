# interpreter -> lib/pkgs/mod/file
import math
import sys
sys.path.append('./')
# > Pkg or pkgmodule (folder) > filemod > function/objs
from m import *
# from m.variables import *
# namespace
# __name__ > dont define then uses default > "__main__"
# __name__ = "myscript"
print("demo:", strvars.name)
print("demo:", type(printme), printme)
printme.funct(strvars.name)
print("demo:", math.sqrt(numvars.num))
print("demo:", __name__)

# Script
if __name__ == "__main__":
    print("demo:","Test Main")
if __name__ == "myscript":
    print("demo:", "Test myscript")


#   from mod import *
#   from mod import name, funct, num
# Scope - for funct not imported will not be available
#   from printme import name, num
# Import of folder path differentiated using . notation
# Imports of modules/filemodules are explicit
# Alias names of modules
#   from m.printme import *
#   from m.variables import num
#   from m import printme as pr
#   from m import printme
#   from m import printme, variables
#   from m.variables import *
# Module name and __name__ are different
# If __name__ is not defined then it will assign modname to __name__ when importing
#     name is defined in the imported file __name__ will be different from mod name
# If __name__ is not defined in the main script file
#       then it will assign __main__ to main script file

# Common Name collisions will happen
# Name overriding depends on when the import statement is used
