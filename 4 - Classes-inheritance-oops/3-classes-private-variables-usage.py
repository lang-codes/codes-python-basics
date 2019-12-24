# Describes how private variables are declared in a class

# Privacy is just a notion and denoted as following:
# __attribute refers to the fact that attribute is private
# _attribute refers protected/private but provided to be accessed outside
# The double '__' refers that it is private
# '__method__(self)' refers to the fact that method is private
# All private references donot stop us from accessing 
#       the private attributes, properties, and methods

# “Private” instance variables that cannot be accessed 
#           except from inside an object don’t exist in Python
# a name prefixed with an underscore (e.g. _spam) 
#           should be treated as a non-public part of the API
# valid use-case for class-private members 
#       (namely to avoid name clashes of names with names defined by subclasses)
# Any identifier of the form __spam (at least two leading underscores, 
#       at most one trailing underscore) is textually replaced with _classname__spam, 
#       where classname is the current class name with leading underscore(s) stripped
#       CALLED name mangling

#  It should be considered an implementation detail 
#           and subject to change without notice


# PRIVATE ATTRIBUTE OR METHOD WITH __ double underscore
class Foo:
    __testPrivateVariableConvention = 1
    def __init__(self, val):
        self.__testPrivateVariableConvention = val
    def printVal(self):
        print("Foo.__testPrivateVariableConvention",self.__testPrivateVariableConvention)
    def setVal(self, val):
        self.__testPrivateVariableConvention = val

test = Foo(12)
test.printVal()
test.setVal(3)
test.printVal()
# __testPrivateVariableConvention will not get set (?? Seems wrong)
test.__testPrivateVariableConvention = 4
print("test.__testPrivateVariableConvention", test.__testPrivateVariableConvention)
test.printVal()

# PRIVATE ATTRIBUTE OR METHOD WITH _ single underscore
class FooBar:
    _testPrivateVariableConvention = 1
    def __init__(self, val):
        self._testPrivateVariableConvention = val
    def printVal(self):
        print("FooBar._testPrivateVariableConvention", self._testPrivateVariableConvention)
    def setVal(self, val):
        self._testPrivateVariableConvention = val

tester = FooBar(12)
tester.printVal()
tester.setVal(3)
tester.printVal()
# tester._testPrivateVariableConvention = 4
print("tester._testPrivateVariableConvention", tester._testPrivateVariableConvention)
tester.printVal()
