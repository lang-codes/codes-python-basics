# HEAD
# Python Basics - Scope rules
# DESCRIPTION
# Describes how Scope rules work in Python with respect to objects
#
# RESOURCES
#


name = "Global Scope"
age = 20

# Defining a function called hello
# Access of variable directly inside function


def hello(global_name):
    global name
    name = "Still global"
    print("hello: global scope", name)
    age = 20
    print("hello: local scope - age (reassigned value)", age)
    print("hello: local scope - global_name (definition passed value)", global_name)


hello(name)


# Class based scoping (Covered in classes in detail)
class Newscope():
    var = "Local Public Scope"
    _var = "Local Protected Scope: Not true protected"
    __var = "Local Private Scope: Not true privacy"

    def __init__(self):
        pass

    def method(self):
        method_local = "Local for method"
        self.var = "Public Local variable for class"

    def _protected_method(self):
        method_local = "Local for method"

    def __private_method(self):
        method_local = "Local for method"


# Class based scoping (Covered in classes in detail)
class InheritedScope():
    inherit = "Local Public Scope"
    _inherit = "Local Protected Scope: Not true protected"
    __inherit = "Local Private Scope: Not true privacy"

    def __init__(self):
        super()

    def method(self):
        method_local = "Local for method"
        self.var = "Public Local variable for class"

    def _protected_method(self):
        method_local = "Local for method"

    def __private_method(self):
        method_local = "Local for method"


