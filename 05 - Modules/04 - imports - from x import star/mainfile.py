# Describes usage of import statements and using a file function as a import

# main module since no __name__ has been specified

# Using * imports to fetch all object definitions
# Will make all the definitions available to the following file
from print import *

# Defining a function called as main
def main():
    printer()
    inputprinter()

if __name__ == '__main__':
    main()