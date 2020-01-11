# Describes creation of Abstract classes in Python
# https://www.smartfile.com/blog/abstract-classes-in-python/

# Usage
# http://masnun.rocks/2017/04/15/interfaces-in-python-protocols-and-abcs/
# https://stackoverflow.com/questions/2736255/abstract-attributes-in-python
# Private Name mangaling error
# https://stackoverflow.com/questions/31457855/cant-instantiate-abstract-class-with-abstract-methods

import abc

class Om(abc.ABC):
    @abc.abstractclassmethod
    def method(cls, args):
        pass
    @abc.abstractclassmethod
    def __contains__(cls, conn=None, structure=None):
        pass

class Hary(Om):
    def __contains__(self, m):
        print(m)
        return True
    def method(cls, args):
        print(args)
        
o = Hary()
# print("test" in o)
o.method(10)

