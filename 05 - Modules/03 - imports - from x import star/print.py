# HEAD
# Modules - Understanding and using import key with file module
# DESCRIPTION
# Describes usage of import statements and 
#       using a file function as a import
# RESOURCES
# 

# print module
# since it is imported into another file the __name__ is
#       assigned with the filename as __name__ value


def printer():
    print('Print Module Called')

def inputprinter():
    print('Enter your name:')
    strs = input()
    print(str(strs))
