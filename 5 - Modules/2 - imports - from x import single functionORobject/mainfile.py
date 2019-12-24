# Describes usage of import statements and using a file function as a import

# Imports only printer function from the print file. Others will not be available
from print import printer

# Defining the main function
def main():
    printer()

# Will run if this file is run since the default value will then be __main__
if __name__ == '__main__':
    main()
