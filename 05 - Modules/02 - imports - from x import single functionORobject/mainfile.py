# HEAD
# Modules - Understanding and using import key 
#       for specific file module scoped object/function/variable
# DESCRIPTION
# Describes usage of import statements and 
#       using a file as a import
# RESOURCES
# 


# Imports only printer function from the print file. Others will not be available
from print import printer

# Defining the main function
def main():
    printer()

# Will run if this file is run since the default value will then be __main__
if __name__ == '__main__':
    main()
