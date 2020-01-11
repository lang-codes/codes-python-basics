# Named Tuples
# https://docs.python.org/2/library/collections.html#collections.namedtuple
# https://stackoverflow.com/questions/39345995/how-does-python-return-multiple-values-from-a-function

import collections

# Create a tuple called NamedTuple
NamedTuple = collections.namedtuple('Point', ['x', 'y'])

p = NamedTuple(1, y=2)

# Access NamedTuple
print(p.x, p.y)
