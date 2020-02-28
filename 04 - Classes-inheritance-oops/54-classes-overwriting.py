# Classes
# Overriding

# Vehicle
class Vehicle():
    maneuver = "Steering"
    body = "Open Top" 
    seats = 4
    wheels = 4
    start = 0
    end = 0
    def __init__(self, maneuver, body, seats, wheels):
        self.maneuver = maneuver
        self.body = body
        self.seats = seats
        self.wheels = wheels
        print("Vehicle Instantiated")
    def move(self, end):
        self.end = end
        print("Vehicle moved from {} to {}".format(self.start, self.end))

# Following is not polymorphism
# v = Vehicle()
# print(v.body, v.maneuver, v.seats, v.wheels, v.start, v.end)
# v = Vehicle("Bike", "Handle", 2, 2)
# print(v.body, v.maneuver, v.seats, v.wheels, v.start, v.end)

class Bike(Vehicle):
    # overriding - Parent-Child scope
    # maneuver = None

    def __init__(self, body, seats, wheels, maneuver= "Handle"):
        # declare => runs automatically when instantiating class
        # defining or assigning value to new 
        #       attribute is like defining it in class
        
        # Use same names in child like parent
        #       overriding => parent:child scoping
        self.maneuver = maneuver
        self.body = body
        self.seats = seats
        self.wheels = wheels
        print("Bike Instantiated")
    
    # overriding - Parent-Child scope
    def move(self, end, name):
        self.end = end
        print("{} moved from {} to {}".format(name, self.start, self.end))

b = Bike("Yamaha", 2, 2)
print(b.body, b.maneuver, b.seats, b.wheels, b.start, b.end)
