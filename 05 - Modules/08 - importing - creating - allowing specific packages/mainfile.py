# Describes usage of import statements and using a file function as a import

# Import traps
# http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html
# main module since no __name__ has been specified

from foo import *

def main():
    inputs.inputprinter()
    print.printer()
    print.inputprinter()

if __name__ == '__main__':
    main()