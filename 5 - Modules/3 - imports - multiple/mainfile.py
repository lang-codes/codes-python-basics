# Describes usage of import statements and using a file function as a import

# main module since no __name__ has been specified

# Using multiple specific imports instead of *
# Will only make the following available to this file
from print import printer, inputprinter

# Defining a function called as main
def main():
    printer()
    inputprinter()

if __name__ == '__main__':
    main()