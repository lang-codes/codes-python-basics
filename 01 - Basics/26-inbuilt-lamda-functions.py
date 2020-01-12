# HEAD
# Inbuilt Lambda Functions
# DESCRIPTION
# Describes some ibuilt lamda functions
# 
# sorted(iterable[, key][, reverse])
# sorted() have a key parameter to specify a
# function to be called on each list element prior to making comparisons
# RESOURCES
# https://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php
# 

from functools import reduce
sortme = [
    ('James', 'Dean', 24),
    ('Jimi', 'Hendrix', 27),
    ('George', 'Gershwin', 38),
]
sorted(sortme, key=lambda age: age[2])

# map(aFunction, aSequence)
# map(function, iterable, ...)
# Return an iterator that applies function to every item of iterable, yielding the results
# If additional iterable arguments are passed, function must take that many arguments
# and is applied to the items from all iterables in parallel.
# With multiple iterables, the iterator stops when the shortest iterable is exhausted.

items = [1, 2, 3, 4, 5]


def sqr(x): return x ** 2


print(list(map(sqr, items)))

# filter(aFunction, aSequence)
print(list(filter((lambda x: x < 0), items)))

# reduce(aFunction, aSequence)
# It accepts an iterator to process, but it's not an iterator itself.
# It returns a single result
# At each step, reduce passes the current product or division,
# along with the next item from the list, to the passed-in lambda function.
# By default, the first item in the sequence initialized the starting value.
print(reduce((lambda x, y: x * y), items))
print(reduce((lambda x, y: x / y), items))
