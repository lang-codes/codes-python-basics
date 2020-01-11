# Describes usage of import statements and using a file function as a import

# Import traps
# http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html
# main module since no __name__ has been specified

import sys

# Check which works, some OS break on using ./path
# sys.path.append('/foo')
sys.path.append('./foo')

from print import *

# Alternatively, if import sys and append foo does not work then you can use the following
# from foo.print import *

# Defining a function called as main
def main():
    printer()
    inputprinter()

if __name__ == '__main__':
    main()
