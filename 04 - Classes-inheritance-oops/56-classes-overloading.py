# Classes
# Overloading

# Overloading using number of args, using default value
def fdefaults(x, y, z, a="Value", b="some", c="other", d="value"):
    # do any operation below whether a,b,c is provided or not
    print(a,y,z,a,b,c)

# Overloading using number of args, using *args
def fargs(*args):
    # do any operation below using args
    if len(args) > 0:
        for i in args:
            print(i)

# Overloading using number of kwargs, using **kwargs
def fkwargs(**kwargs):
    # do any operation below using kwargs
    if len(kwargs.keys()) > 0:
        for i in kwargs:
            print(i)

# Overloading using number of args & kwargs, using **kwargs
def fargskwargs(*args, **kwargs):
    # do any operation below using args, kwargs
    if len(args):
        for i in args:
            print(i)
    if len(kwargs.keys()) > 0:
        for i in kwargs:
            print(i)

# Overloading within classes - different ways
class Vehicle():
    start = 0
    end = 0
    def move(self, end):
        self.end = end
        print("Vehicle moved from {} to {}".format(self.start, self.end))

class Bike(Vehicle):    
    # overriding - Parent-Child scope
    def move(self, end):
        self.end = end
        name = "Bike"
        print("{} moved from {} to {}".format(name, self.start, self.end))

    # Overloading using number of args, using default value
    def fdefaults(self, x, y, z, a="Value", b="some", c="other", d="value"):
        # do any operation below whether a,b,c is provided or not
        print(a,y,z,a,b,c)

    # Overloading using number of args, using *args
    def fargs(self, *args):
        # do any operation below using args
        if len(args) > 0:
            for i in args:
                print(i)

    # Overloading using number of kwargs, using **kwargs
    def fkwargs(self, **kwargs):
        # do any operation below using kwargs
        if len(kwargs.keys()) > 0:
            for i in kwargs:
                print(i)

    # Overloading using number of args & kwargs, using **kwargs
    def fargskwargs(self, *args, **kwargs):
        # do any operation below using args, kwargs
        if len(args):
            for i in args:
                print(i)
        if len(kwargs.keys()) > 0:
            for i in kwargs:
                print(i)


