# HEAD
# Classes Introduction - Initialization Method with attributes
# DESCRIPTION
# Describes how to create initialization method with attributes
# Initialization Function - Init method with attributes
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
    # 
    # # Follows all rules of functions but has 
    #           self as first arg for passing instance reference
    #           Can hold args, kwargs (during invocation)
    #               def __init__(self, val, newAttr) 
    #               Invoked as:
    #                   MethodInit(10, 20)
    #                   MethodInit(10, newAttr = 20)
    #                   MethodInit(attr = 10, newAttr = 20)
    #           Can hold default value declaration
    #               def __init__(self, val="default value during declaration")
    #           Can hold *args declaration
    #               def __init__(self, *args)
    #           Can hold **kwargs declaration
    #               def __init__(self, **kwargs)
    # 
    def __init__(self, val, newAttr):
        
        # Reassigns default value provided for attr inside class
        self.attr = 10
        print("Init method invoked")
        print("attr assigned with new value ", self.attr)
        
        # Equivalent to making a new attribute within class 
        #       named newAttr
        self.newAttr = newAttr
        print("newAttr assigned with new value ", self.newAttr)


obj = MethodInit(10, 20)

