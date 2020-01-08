# Concept implementing Simple Inheritence 
#       with passage of args to one parent 
#       using super().__init(arg)

class Body:
    body = None
    def __init__(self, body):
        self.body = body

    def set_body(self, value):
        self.body = value
    
    def get_body(self):
        return self.body

# Inheritance from single parent Body
# We can have no base/parent or 'n'/many of them
class Bike(Body):
    handle = None
    wheel = None
    # Super applies to the first parent
        # super() below is optional
        # Inheritence does not need super()
        #    to be explicit
        # super()
        # To pass simple args or kwargs
        # super.__init__(*args, **kwargs)
    def __init__(self, handle, wheel, body,seats):
        super().__init__(seats)
        self.handle = handle
        self.wheel = wheel

bike = Bike("Thin", 5.5, "Terrain Bike", 2)
# Now access the object
# bike.