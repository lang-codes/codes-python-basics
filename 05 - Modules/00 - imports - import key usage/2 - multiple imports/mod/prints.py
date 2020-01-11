# Describes the usage of the file as a module (not as a script file)

# Declaring the printer function
def printer():
    print('Print Module Called')


if __name__ == '__main__':
    printer()
    print("Triggered from __name__ == '__main__' of print")

