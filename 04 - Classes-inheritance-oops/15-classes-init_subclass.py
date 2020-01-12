# HEAD
# Classes - __init_subclass__() method
# DESCRIPTION
# Describes usage of __init_subclass__ method
# RESOURCES
# 


# # Variation
# # https://docs.python.org/3/reference/datamodel.html#implementing-descriptors
# class Philosopher:
#     def __init_subclass__(cls, default_name, **kwargs):
#         super().__init_subclass__(**kwargs)
#         cls.default_name = default_name

# class AustralianPhilosopher(Philosopher, default_name="Bruce"):
#     pass

# Sample codes
# https://gist.github.com/pjeby/75ca26f8d2a7a0c68e30

# VARIATION2 - Accessing superparent variable
# https://stackoverflow.com/questions/53189980/accessing-superparent-class-variable-in-python
# VARIATION3 - Static methods
# https://stackabuse.com/object-oriented-programming-in-python/

# Describing a base class called as WheelType
class WheelType:
    # Defining the private attribute/property __type
    __type = "round"

    # Defining __init__ or constructor
    def __init__(self, val):
        self.__type = val

    # Defining the __init_subclass__ taking statistically defined argument, keyword arguments
    def __init_subclass__(self, wType, **kwargs):
        super().__init_subclass__(**kwargs)
        self.__type = wType
        print('**kwargs WT', kwargs)

    # Defining a simple getter for wheel __type
    def get_wheel_type(self):
        return self.__type

    # Defining a simple setter for wheel __type
    def set_wheel_type(self, prop):
        self.__type = prop


# Describing a base class called as EngineType
class EngineType:
    # Defining the private attributes/properties __engineType
    __engineType = "jeep"

    # Defining the __init_subclass__ taking staically defined argument, keyword arguments
    def __init_subclass__(self, eType, **kwargs):
        super().__init_subclass__(**kwargs)
        self.__engineType = eType
        print('**kwargs ET', kwargs)

    # Defining __init__ taking the value of the __engineType
    def __init__(self, val):
        self.__engineType = val

    # Defining a simple getter for Engine __engineType
    def getEngineType(self):
        return self.__engineType

    # Defining a simple setter for Engine __engineType
    def setEngineType(self, val):
        self.__engineType = val


# Defining a Vehicle class that extends EngineType, WheelType (MULTIPLE INHERITANCE)
# Also adds __init_subclass__ keyword arguments for parents implementing subclass function
# __init_subclass__ keyword arguments have to be declared in the parents else throws error
# **kwargs is buggy without declaring __init_subclass__ keyword > Rectify this with a bug ticket
#
class Vehicle(EngineType, WheelType, eType="Test", wType="Tester"):
    # Creating two private attributes/properties for __otherParts
    __otherParts = ["bonet", "dicky", "rooftop"]
    __pendingParts = ["seats", "stearing"]

    # Defining the __init__ method
    def __init__(self, ppart, eType, wType):
        # Instantiate parent - does first parent class instantiation
        # Second parent class also has to do super to init second parent
        # Or use specific Base call instantiators as below
        # super()

        # When you have one Parent or Base class
        # super().__init__(eType)

        # When you have multiple Base or Parent class, pass arguments
        # EngineType.__init__(self, eType)
        # WheelType.__init__(self, wType)

        self.eType = eType
        self.__pendingParts.append(ppart)

    # Defining setter method for __pendingParts
    def set_pendingParts(self, val):
        self.__pendingParts = val

    # Defining getter method for __pendingParts
    def get_pendingPats(self):
        return self.__pendingParts

    # Defining getter method for multiple values
    def get_vehicle(self):
        return self.getEngineType(), self.__otherParts, self.__pendingParts

    # Defining setter method for multiple values
    def set_vehicle(self, et, oParts, pParts):
        self.setEngineType(et)
        self.__otherParts = oParts
        self.__pendingParts = pParts


# Instantiation of Vehicle class
vh = Vehicle("pPart", "Car", "Square")

# Checking for properties to be available and function
print(vh.getEngineType())
print(vh.get_wheel_type())
