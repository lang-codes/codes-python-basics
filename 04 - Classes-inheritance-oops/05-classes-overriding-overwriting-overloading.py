# Describes overiding, overwriting, and overloading concepts

# OVERWRITING
# def funct():
#     pass

# def funct():
#     print('val')

# OVERLOADING - Theoritically not possible in python classes
# Using different forms of function execution implementation
# https://overiq.com/python-101/operator-overloading-in-python/
# Due to absence of types
# def getInt(val):
#     print(val)
# def getInt(str(val), someotherval):
#     print(val)


# OVERRIDING
# parent class with printVal function
class Foo:
    def __init__(self, val):
        self.val = val

    def printVal(self):
        print(self.val)

# Overriding printVal of Foo into its own implementation
class DerivedFoo2(Foo):

    def printVal(self):
        print('DerivedFoo2: My value is %s' % self.val)

df1 = DerivedFoo2(12)
df1.printVal()

# Overloading printVal of Foo into its own implementation
# This DOES NOT work in Python
# There is an alternative mentioned in DerivedFoo4
class DerivedFoo3:
    val = "DerivedFoo3: TestOver Loading Concept - Normal Usage"
    # TypeError due to wrong number of 
    #       arguments in the function
    # df3.printVal()
    def printVal(self):
        print('DerivedFoo3 - Doesnt work: My value is %s' % self.val)
    # This is taken as the real implementation due to overwriting
    def printVal(self, arg):
        print('DerivedFoo3: My value is %s' % self.val, " - ", arg)

df3 = DerivedFoo3()
# TypeError due to wrong number of 
#       arguments in the function
# df3.printVal()
df3.printVal("DerivedFoo3")

# Overloading printVal of Foo in Python - Real working implementation
class DerivedFoo4:
    val = "DerivedFoo4: TestOver Loading Concept - Normal Usage"
    def printVal(self, val="Provide Default DerivedFoo4"):
        print('DerivedFoo4: My value is %s' % self.val)
    
df41 = DerivedFoo4()
df41.printVal()

df42 = DerivedFoo4()
df42.printVal("DerivedFoo4")


# Overloading printVal of Foo in Python - Real working implementation
class DerivedFoo5:
    val = "DerivedFoo5: TestOver Loading Concept - Normal Usage"
    def printVal(self, arg="Provide Default DerivedFoo4"):
        print('DerivedFoo5: My value is %s' % self.val, " - ", arg)

df51 = DerivedFoo5()

# Takes the default value in the function definition
df51.printVal()

df52 = DerivedFoo5()
df52.printVal("DerivedFoo5")


# Overloading printVal of Foo in Python - Real working implementation
class DerivedFoo6:
    val = "DerivedFoo6: TestOver Loading Concept - Normal Usage"
    
    # Overloading
    def printVal(self, arg="Provide Default DerivedFoo4"):
        print('DerivedFoo6: My value is %s' % self.val, " - ", arg)

df61 = DerivedFoo6()

# Works - Takes the default Provided value in the function definition
# Overloading - 1
df61.printVal()

df62 = DerivedFoo6()
# Works - Takes the value in the function invocation
# Overloading - 2
df62.printVal("DerivedFoo6")


# Overloading printVal of Foo in Python - Real working implementation
class DerivedFoo7:
    val = "DerivedFoo6: TestOver Loading Concept - Normal Usage"
    
    # Overloading
    def printVal(self, arg=None):
        if arg == None:
            print('DerivedFoo6: My value is %s' % self.val, " - NoneType")
        else:
            print('DerivedFoo6: My value is %s' % self.val, " - ", arg)

df61 = DerivedFoo7()

# Works - Takes the default value in the function definition
# Overloading - 1
df61.printVal()

# Works - Takes the value in the function invocation
# Overloading - 2
df61.printVal("DerivedFoo6")



