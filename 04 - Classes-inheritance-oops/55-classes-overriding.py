# Classes
# Overwriting

def func():
    pass

# Overwriting - same scope, same name, and gets overwritten
def func(a):
    print(a)

# Vehicle
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
    
    # Following same scope, same name, and gets overwritten
    # Following overwrites above move(self, end) method of 
    #       child using method move(self, end, name) below
    def move(self, end, name):
        self.end = end
        print("{} moved from {} to {}".format(name, self.start, self.end))

b = Bike("Yamaha", 2, 2)

