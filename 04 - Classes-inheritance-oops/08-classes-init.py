# HEAD
# Classes Introduction - Initialization Method
# DESCRIPTION
# Describes how to create a initialization method
# Initialization Function - Init method
# __init__
# RESOURCES
# 


class MethodInit():
    # An class attribute with "somevalue"
    attr = "somevalue"

    # # Following method __init__() is called
    #   Instantiator
    #   Initialiser Method
    #   Constructor
    def __init__(self):
        # Reassigns default value provided
        self.attr = 10
        print("Init method invoked & attr assigned with new value ", self.attr)


obj = MethodInit()


