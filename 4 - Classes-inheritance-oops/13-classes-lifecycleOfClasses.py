# Describes the simple lifecycle of classes

class LifeCycleClass:

    # New function is triggered first before the object is formed
    # def __new__(cls, *args, **kwargs):
    #     print("First function __new__ to be triggered in class life cycle: LifeCycleClass")
    #     # Has to return the cls since this is triggered before the object is completely ready
    #     return cls

    # First function to be triggered after the object is being created
    def __init__(self, val):
        print("Second function __init__ to be triggered in class life cycle: LifeCycleClass", val)
        # Testing call method
        self.__call__()

    # Call the method to run execution block
    def __call__(self):
        print("Third function __call__ to be triggered in class life cycle: LifeCycleClass")

    # Last function to be triggered and is done during the object is being destroyed
    def __del__(self):
        print("Last function __del__ to be triggered in class life cycle: LifeCycleClass")

    # Call the function to destroy the instance of the class
    def __delete__(self, instance):
        print("Function __delete__ to be triggered manually to delete in class life cycle: LifeCycleClass")

# Creating the instance of class LifeCycleClass
obj = LifeCycleClass('Testing init')
# All the functions should be triggered by the end of exit of the process
# print(obj)

