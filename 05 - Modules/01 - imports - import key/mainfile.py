# Describes usage of import statements and using a file as a import

# Describes what is a main module
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do

# Find and load a module given its string name, "math",
# then assign it to a local variable called math.
# Below line of code `import print` is equivalent to print
# print = __import__("print")

import print

# Alternatively, you can use a different name for the above statement, like below
# import print as pt

def main():
    print.printer()
    print.inputprinter()
    print("Triggered from main() of mainfile")

if __name__ == '__main__':
    main()

# project/
# │
# ├── my_sum/
# │   └── __init__.py
# |
# └── test.py

# target = __import__("my_sum.py")
# sum = target.sum
