# HEAD
# Classes - Magic Methods - Copying
# DESCRIPTION
# Describes the magic methods of classes 
#       copy(), deepcopy()
# RESOURCES
# 
# https://rszalski.github.io/magicmethods/


# Copying

# Sometimes, particularly when dealing with mutable objects, you want to be able to copy an object and make changes without affecting what you copied from. This is where Python's copy comes into play. However (fortunately), Python modules are not sentient, so we don't have to worry about a Linux-based robot uprising, but we do have to tell Python how to efficiently copy things.

# __copy__(self)
#     Defines behavior for copy.copy() for instances of your class. copy.copy() returns a shallow copy of your object -- this means that, while the instance itself is a new instance, all of its data is referenced -- i.e., the object itself is copied, but its data is still referenced (and hence changes to data in a shallow copy may cause changes in the original).
# __deepcopy__(self, memodict={})
#     Defines behavior for copy.deepcopy() for instances of your class. copy.deepcopy() returns a deep copy of your object -- the object and its data are both copied. memodict is a cache of previously copied objects -- this optimizes copying and prevents infinite recursion when copying recursive data structures. When you want to deep copy an individual attribute, call copy.deepcopy() on that attribute with memodict as the first argument.

# What are some use cases for these magic methods? As always, in any case where you need more fine-grained control than what the default behavior gives you. For instance, if you are attempting to copy an object that stores a cache as a dictionary (which might be large), it might not make sense to copy the cache as well -- if the cache can be shared in memory between instances, then it should be.


