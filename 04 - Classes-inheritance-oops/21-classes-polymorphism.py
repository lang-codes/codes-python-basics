# HEAD
# Classes - Polymorphism
# DESCRIPTION
# Describe the concept of polymorphism in a simple way
# Manual getter, setter for private (private notation) attr/props
# RESOURCES
# 


class CommonVehicleAttributes:
    # Describe type of wheel specific to vehicle
    __wheelType = None
    # Describe type of chasis specific to vehicle
    __chasis = None
    # Describe type of engine specific to vehicle
    __EngineType = None
    # Describe type of seatc specific to vehicle
    __Seat = None

    def __init__(self, wt, ch, et, st):
        pass

    # Simple getter for wheel type
    def get_wheel_type(self):
        return self.__wheelType

    # Simple setter for wheel type
    def set_wheel_type(self, val):
        self.__wheelType = val

    # Simple getter for chasis type
    def get_chasis_type(self):
        return self.__chasis

    # Simple setter for chasis type
    def set_chasis_type(self, val):
        self.__chasis = val

    # Simple getter for engine type
    def get_engine_type(self):
        return self.__EngineType

    # Simple setter for engine type
    def set_engine_type(self, val):
        self.__EngineType = val

    # Simple getter for seat type
    def get_seat_type(self):
        return self.__Seat

    # Simple setter for seat type
    def set_seat_type(self, val):
        self.Seat = val


class Bike(CommonVehicleAttributes):
    # Take the details of handle type
    __handle = "Bike"

    def __init__(self, wt, ch, et, st, hd):
        super().__init__(wt, ch, et, st)
        self.__handle = hd

    # Simple getter for handle type
    def get_handle_type(self):
        return self.__handle

    # Simple setter for handle type
    def set_handle_type(self, val):
        self.__handle = val


class Car(CommonVehicleAttributes):
    # Take the details of bonet type
    __bonet = None
    # Take the details of dicky type
    __dicky = None

    def __init__(self, wt, ch, et, st, bt, dk):
        super().__init__(wt, ch, et, st)
        self.__bonet = bt
        self.__dicky = dk

    # Simple getter for handle type
    def get_bonet_type(self):
        return self.__bonet

    # Simple setter for dicky type
    def set_bonet_type(self, val):
        self.__bonet = val

    # Simple getter for handle type
    def get_dicky_type(self):
        return self.__dicky

    # Simple setter for dicky type
    def set_dicky_type(self, val):
        self.__dicky = val


class Jeep(CommonVehicleAttributes):
    # Take the details of bonet type
    __bonet = None

    def __init__(self, wt, ch, et, st, bt):
        super().__init__(wt, ch, et, st)
        self.__bonet = bt

    # Simple getter for handle type
    def get_bonet_type(self):
        return self.__bonet

    # Simple setter for handle type
    def set_bonet_type(self, val):
        self.__bonet = val

# Now instantiate the forms or morphs of CommonVehicleAttributes
jeepVehicle = Jeep("JeepRound", "Sturdy", {'ignition': 6, 'capacity': 20, 'bhp': 85}, "Multiple", "Aerodynamic")

# Getting the object attributes and methods
print(jeepVehicle.__dict__)
