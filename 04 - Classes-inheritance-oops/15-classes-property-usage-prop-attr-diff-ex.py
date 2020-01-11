# Describes creating of getters and setters in an alternative way

# Internet says attributes and properties are interchangable 
# and methods are seperate class functions

# Defining Class C
class C:
    # Defining __init__
    def __init__(self):
        # Defining a property for _x
        self._x = "Test"

    # Defining a getter for _x
    def getx(self):
        return self._x

    # Defining a setter for _x
    def setx(self, value):
        self._x = value

    # Defining a del function for _x
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

# If c is an instance of C, 
# c.x will invoke the getter, 
# c.x = value will invoke the setter and 
# del c.x the deleter
#
# def setprop(self, prop):
#     self._prop = prop
# def getprop(self):
#     return self._prop

obj = C()
print(obj.x)
obj.x = 10
print(obj.x)