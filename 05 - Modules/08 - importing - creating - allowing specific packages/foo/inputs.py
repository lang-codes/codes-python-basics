def inputprinter():
    print('Enter your name:')
    strs = input()
    print(str(strs))

if __name__ == '__main__':
    # Remember the console will wait for your input
    inputprinter()
    print("Triggered from __name__ == '__main__' of print")

