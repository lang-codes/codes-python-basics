# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Concept implementing multiple inheritence 
#       with passage of args to two parents
#       and usage of super().__init__(args)
#       Parent.__init__(self, args)
# RESOURCES
# 


class Body:
    body = None

    def __init__(self, body):
        self.body = body

    def set_body(self, value):
        self.body = value

    def get_body(self):
        return self.body

class Parts:
    seats = None

    def __init__(self, seats):
        self.seats = seats

    def get_seats(self):
        return self.seats
    def set_seats(self, value):
        self.seats = value
        
class Bike(Parts, Body):
    handle = None
    wheel = None

    def __init__(self, handle, wheel, body, seats):
        # Super applies to the first parent
        super().__init__(seats)
        # For second parent you have to do a explict 
        #       instantiation with name of class
        Body.__init__(self, body)
        self.handle = handle
        self.wheel = wheel

bike = Bike("Thin", 5.5, "Terrain Bike", 2)
# Now access the object
# bike.