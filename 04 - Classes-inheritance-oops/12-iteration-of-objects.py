# Describes creating an object that behaves like an iterator object
# We have to define a __iter__ method and __next__ method

# Backwards iteration of class object
class Backwards:
    def __init__(self, val):
        self.val = val
        self.pos = len(val)
    def __iter__(self):
        return self
    def __next__(self):
        if self.pos <= 0:
            raise StopIteration
        self.pos = self.pos - 1
        return self.val[self.pos]

# using class iterator created
for item in Backwards('Tester'):
        print(item)
