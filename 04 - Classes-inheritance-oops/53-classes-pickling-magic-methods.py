# HEAD
# Classes - Pickling Concept
# DESCRIPTION
# Describes the magic methods of classes
#       getinitargs, getnewargs, 
#       getstate, setstate, 
#       reduce, reduce_ex
# RESOURCES
# 
# https://rszalski.github.io/magicmethods/


# Pickling your own Objects

# Pickling isn't just for built-in types. 
# It's for any class that follows the pickle protocol. 
# The pickle protocol has four optional methods for Python 
#       objects to customize how they act (it's a bit 
#       different for C extensions, but that's not in our scope):

# __getinitargs__(self)
#     If you'd like for __init__ to be called when your class is unpickled, you can define __getinitargs__, which should return a tuple of the arguments that you'd like to be passed to __init__. Note that this method will only work for old-style classes.
# __getnewargs__(self)
#     For new-style classes, you can influence what arguments get passed to __new__ upon unpickling. This method should also return a tuple of arguments that will then be passed to __new__.
# __getstate__(self)
#     Instead of the object's __dict__ attribute being stored, you can return a custom state to be stored when the object is pickled. That state will be used by __setstate__ when the object is unpickled.
# __setstate__(self, state)
#     When the object is unpickled, if __setstate__ is defined the object's state will be passed to it instead of directly applied to the object's __dict__. This goes hand in hand with __getstate__: when both are defined, you can represent the object's pickled state however you want with whatever you want.
# __reduce__(self)
#     When defining extension types (i.e., types implemented using Python's C API), you have to tell Python how to pickle them if you want them to pickle them. __reduce__() is called when an object defining it is pickled. It can either return a string representing a global name that Python will look up and pickle, or a tuple. The tuple contains between 2 and 5 elements: a callable object that is called to recreate the object, a tuple of arguments for that callable object, state to be passed to __setstate__ (optional), an iterator yielding list items to be pickled (optional), and an iterator yielding dictionary items to be pickled (optional).
# __reduce_ex__(self)
#     __reduce_ex__ exists for compatibility. If it is defined, __reduce_ex__ will be called over __reduce__ on pickling. __reduce__ can be defined as well for older versions of the pickling API that did not support __reduce_ex__.

# An Example

# Our example is a Slate, which remembers what its values 
#       have been and when those values were written to it. 
#       However, this particular slate goes blank each time 
#       it is pickled: the current value will not be saved.

# import time

# class Slate:
#     '''Class to store a string and a changelog, and forget its value when
#     pickled.'''

#     def __init__(self, value):
#         self.value = value
#         self.last_change = time.asctime()
#         self.history = {}

#     def change(self, new_value):
#         # Change the value. Commit last value to history
#         self.history[self.last_change] = self.value
#         self.value = new_value
#         self.last_change = time.asctime()

#     def print_changes(self):
#         print 'Changelog for Slate object:'
#         for k, v in self.history.items():
#             print '%s\t %s' % (k, v)

#     def __getstate__(self):
#         # Deliberately do not return self.value or self.last_change.
#         # We want to have a "blank slate" when we unpickle.
#         return self.history

#     def __setstate__(self, state):
#         # Make self.history = state and last_change and value undefined
#         self.history = state
#         self.value, self.last_change = None, None

# Conclusion

# The goal of this guide is to bring something to anyone that reads it, regardless of their experience with Python or object-oriented programming. If you're just getting started with Python, you've gained valuable knowledge of the basics of writing feature-rich, elegant, and easy-to-use classes. If you're an intermediate Python programmer, you've probably picked up some slick new concepts and strategies and some good ways to reduce the amount of code written by you and clients. If you're an expert Pythonista, you've been refreshed on some of the stuff you might have forgotten about and maybe picked up a few new tricks along the way. Whatever your experience level, I hope that this trip through Python's special methods has been truly magical. (I couldn't resist the final pun!)
# Appendix 1: How to Call Magic Methods

# Some of the magic methods in Python directly map to built-in functions; in this case, how to invoke them is fairly obvious. However, in other cases, the invocation is far less obvious. This appendix is devoted to exposing non-obvious syntax that leads to magic methods getting called.
# Magic Method 	When it gets invoked (example) 	Explanation
# __new__(cls [,...]) 	instance = MyClass(arg1, arg2) 	__new__ is called on instance creation
# __init__(self [,...]) 	instance = MyClass(arg1, arg2) 	__init__ is called on instance creation
# __cmp__(self, other) 	self == other, self > other, etc. 	Called for any comparison
# __pos__(self) 	+self 	Unary plus sign
# __neg__(self) 	-self 	Unary minus sign
# __invert__(self) 	~self 	Bitwise inversion
# __index__(self) 	x[self] 	Conversion when object is used as index
# __nonzero__(self) 	bool(self) 	Boolean value of the object
# __getattr__(self, name) 	self.name # name doesn't exist 	Accessing nonexistent attribute
# __setattr__(self, name, val) 	self.name = val 	Assigning to an attribute
# __delattr__(self, name) 	del self.name 	Deleting an attribute
# __getattribute__(self, name) 	self.name 	Accessing any attribute
# __getitem__(self, key) 	self[key] 	Accessing an item using an index
# __setitem__(self, key, val) 	self[key] = val 	Assigning to an item using an index
# __delitem__(self, key) 	del self[key] 	Deleting an item using an index
# __iter__(self) 	for x in self 	Iteration
# __contains__(self, value) 	value in self, value not in self 	Membership tests using in
# __call__(self [,...]) 	self(args) 	"Calling" an instance
# __enter__(self) 	with self as x: 	with statement context managers
# __exit__(self, exc, val, trace) 	with self as x: 	with statement context managers
# __getstate__(self) 	pickle.dump(pkl_file, self) 	Pickling
# __setstate__(self) 	data = pickle.load(pkl_file) 	Pickling

