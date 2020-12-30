# HEAD
# Python Basics - Implementing Switch statements in Python
# DESCRIPTION
# Describes how to Implement Switch statements in Python
#       Python doesnt support switch statement officially
#       Only Alternate methods are available
# 
# RESOURCES
#


# Alternative methods involve creating a dictionary
#         and fetching information or function
#         implementation from them
def zero():
    return 'zero'


def one():
    return 'one'


def indirect(i):
    switcher = {
        0: zero,
        1: one,
        2: lambda: 'two'
    }
    func = switcher.get(i, lambda: 'Invalid')
    return func()


# Run the switch as a method
indirect(4)


# Second alternative method is creating a class
#       with class methods as switch implements. The choices
#       can then be invoked using a method invoker
# TODO: SWITCH FUNCTION
class Switcher(object):
    def indirect(self, i):
        method_name = 'number_'+str(i)
        method = getattr(self, method_name, lambda: 'Invalid')
        return method()

    def switch(self, val):
        method = getattr(self, val, lambda: 'Invalid')
        return method()

    def number_0(self):
        return 'zero'

    def number_1(self):
        return 'one'

    def number_2(self):
        return 'two'


s = Switcher()

# Run the switch as a method
s.indirect(2)
s.switch(2)
