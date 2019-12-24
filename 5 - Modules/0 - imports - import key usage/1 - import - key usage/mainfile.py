# import statement, variations of import
# __name__

# |----- /mod -----
# |                |
# |                |----- printfile.py
# |
# |----- mainfile.py

# USING as a script file (running the file as a script)
# Considers the script file to be within folder `mod` named `printfile.py`
# Considers the main file importing the script file to be outside the `mod` folder and in the same level

# When __name__ is not assigned:
#   default value for __name__ assigned will be __main__
# When __name__ is assigned:
#   value assigned for __name__ will be the one provided

# When you have `if name == "value"` statements
# One that will be triggered will be the one that matches

# USING the file as a module (running a different file that imports the file specified)
# Considers the script file to be within folder `mod` named `printfile.py`
# Considers the main file importing the script file to be outside the `mod` folder and in the same level


# When __name__ is not assigned:
#   default value for module will be generally filename or path.filename
#       (based on whether it will be within the same folder or within different folder)
#   default value for __name__ assigned will be name of the module
# When __name__ is assigned:
#   value assigned for __name__ will be the one provided
#   module name will be take as filename or path.filename, which will be used for import statement
#       (based on whether it will be within the same folder or within different folder)

# When you import the file into a different file
#       and __name__ is assigned a different value then
#       it will not be triggering `if __name__ == "__main__"` block and
#       it will be triggering `if __name__ == "providedvalue"` block


# DIFFERENT FORMS OF USAGES

# WAY ONE
# import mod.filename as pr
# from mod import filename as pr

# WAY TWO
# import mod.filename
# from mod import filename

# WAY THREE
# import sys
#
# sys.path.append('./mod/')
# import filename


# WAY FOUR
# import sys
#
# sys.path.append('./')
# import mod.filename


# WAY FIVE
# all obj will be available in the global space
# including __name__. Hence, overridden

# from mod.filename import *


# WAY SIX
# Will only import func and func_two obj

# from mod.filename import func, func_two


# Wrong
# from mod.filename import * as pr





print('__name__', __name__)
print('mod.filename.__name__', __name__)
