# Describes the magic methods of classes
# https://rszalski.github.io/magicmethods/

# Making Custom Sequences

# There's a number of ways to get your Python classes to act like built in sequences (dict, tuple, list, str, etc.). These are by far my favorite magic methods in Python because of the absurd degree of control they give you and the way that they magically make a whole array of global functions work beautifully on instances of your class. But before we get down to the good stuff, a quick word on requirements.
# Requirements

# Now that we're talking about creating your own sequences in Python, it's time to talk about protocols. Protocols are somewhat similar to interfaces in other languages in that they give you a set of methods you must define. However, in Python protocols are totally informal and require no explicit declarations to implement. Rather, they're more like guidelines.

# Why are we talking about protocols now? Because implementing custom container types in Python involves using some of these protocols. First, there's the protocol for defining immutable containers: to make an immutable container, you need only define __len__ and __getitem__ (more on these later). The mutable container protocol requires everything that immutable containers require plus __setitem__ and __delitem__. Lastly, if you want your object to be iterable, you'll have to define __iter__, which returns an iterator. That iterator must conform to an iterator protocol, which requires iterators to have methods called __iter__(returning itself) and next.
# The magic behind containers

# Without any more wait, here are the magic methods that containers use:

# __len__(self)
#     Returns the length of the container. Part of the protocol for both immutable and mutable containers.
# __getitem__(self, key)
#     Defines behavior for when an item is accessed, using the notation self[key]. This is also part of both the mutable and immutable container protocols. It should also raise appropriate exceptions: TypeError if the type of the key is wrong and KeyError if there is no corresponding value for the key.
# __setitem__(self, key, value)
#     Defines behavior for when an item is assigned to, using the notation self[nkey] = value. This is part of the mutable container protocol. Again, you should raise KeyError and TypeError where appropriate.
# __delitem__(self, key)
#     Defines behavior for when an item is deleted (e.g. del self[key]). This is only part of the mutable container protocol. You must raise the appropriate exceptions when an invalid key is used.
# __iter__(self)
#     Should return an iterator for the container. Iterators are returned in a number of contexts, most notably by the iter() built in function and when a container is looped over using the form for x in container:. Iterators are their own objects, and they also must define an __iter__ method that returns self.
# __reversed__(self)
#     Called to implement behavior for the reversed() built in function. Should return a reversed version of the sequence. Implement this only if the sequence class is ordered, like list or tuple.
# __contains__(self, item)
#     __contains__ defines behavior for membership tests using in and not in. Why isn't this part of a sequence protocol, you ask? Because when __contains__ isn't defined, Python just iterates over the sequence and returns True if it comes across the item it's looking for.
# __missing__(self, key)
#     __missing__ is used in subclasses of dict. It defines behavior for whenever a key is accessed that does not exist in a dictionary (so, for instance, if I had a dictionary d and said d["george"] when "george" is not a key in the dict, d.__missing__("george") would be called).

# An example

# For our example, let's look at a list that implements some functional constructs that you might be used to from other languages (Haskell, for example).

# class FunctionalList:
#     '''A class wrapping a list with some extra functional magic, like head,
#     tail, init, last, drop, and take.'''

#     def __init__(self, values=None):
#         if values is None:
#             self.values = []
#         else:
#             self.values = values

#     def __len__(self):
#         return len(self.values)

#     def __getitem__(self, key):
#         # if key is of invalid type or value, the list values will raise the error
#         return self.values[key]

#     def __setitem__(self, key, value):
#         self.values[key] = value

#     def __delitem__(self, key):
#         del self.values[key]

#     def __iter__(self):
#         return iter(self.values)

#     def __reversed__(self):
#         return reversed(self.values)

#     def append(self, value):
#         self.values.append(value)
#     def head(self):
#         # get the first element
#         return self.values[0]
#     def tail(self):
#         # get all elements after the first
#         return self.values[1:]
#     def init(self):
#         # get elements up to the last
#         return self.values[:-1]
#     def last(self):
#         # get last element
#         return self.values[-1]
#     def drop(self, n):
#         # get all elements except first n
#         return self.values[n:]
#     def take(self, n):
#         # get first n elements
#         return self.values[:n]

# There you have it, a (marginally) useful example of how to implement your own sequence. Of course, there are more useful applications of custom sequences, but quite a few of them are already implemented in the standard library (batteries included, right?), like Counter, OrderedDict, and NamedTuple.

