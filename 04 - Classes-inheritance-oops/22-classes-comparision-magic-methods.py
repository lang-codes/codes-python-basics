# HEAD
# Classes - Magic Methods - Comparison Methods
# DESCRIPTION
# Describes the magic methods of classes
#        call, init
# RESOURCES
# 
# https://rszalski.github.io/magicmethods/

# Comparison magic methods

# Python has a whole slew of magic methods designed to implement intuitive comparisons between objects using operators, not awkward method calls. They also provide a way to override the default Python behavior for comparisons of objects (by reference). Here's the list of those methods and what they do:

# __cmp__(self, other)
#     __cmp__ is the most basic of the comparison magic methods. 
#       It actually implements behavior for all of 
#       the comparison operators (<, ==, !=, etc.), 
#       but it might not do it the way you want (for example, 
#       if whether one instance was equal to another were determined 
#       by one criterion and and whether an instance is greater 
#       than another were determined by something else). 
#       __cmp__ should return a negative integer if 
#       self < other, zero if self == other, and positive 
#       if self > other. It's usually best to define each 
#       comparison you need rather than define them all at once, 
#       but __cmp__ can be a good way to save repetition and improve clarity 
#       when you need all comparisons implemented with similar criteria.
# __eq__(self, other)
#     Defines behavior for the equality operator, ==.

# __ne__(self, other)
#     Defines behavior for the inequality operator, !=.

# __lt__(self, other)
#     Defines behavior for the less-than operator, <.

# __gt__(self, other)
#     Defines behavior for the greater-than operator, >.

# __le__(self, other)
#     Defines behavior for the less-than-or-equal-to operator, <=.

# __ge__(self, other)
#     Defines behavior for the greater-than-or-equal-to operator, >=.

# For an example, consider a class to model a word. 
# We might want to compare words lexicographically (by the alphabet), 
# which is the default comparison behavior for strings, 
# but we also might want to do it based on some other criterion, 
# like length or number of syllables. In this example, 
# we'll compare by length. Here's an implementation:

# class Word(str):
#     '''Class for words, defining comparison based on word length.'''
#     def __new__(cls, word):
#         # Note that we have to use __new__. This is because str is an immutable
#         # type, so we have to initialize it early (at creation)
#         if ' ' in word:
#             print "Value contains spaces. Truncating to first space."
#             word = word[:word.index(' ')] # Word is now all chars before first space
#         return str.__new__(cls, word)
#     def __gt__(self, other):
#         return len(self) > len(other)
#     def __lt__(self, other):
#         return len(self) < len(other)
#     def __ge__(self, other):
#         return len(self) >= len(other)
#     def __le__(self, other):
#         return len(self) <= len(other)

# Now, we can create two Words (by using Word('foo') and Word('bar')) and 
# compare them based on length. Note, however, that we didn't define __eq__ and __ne__. 
# This is because this would lead to some weird behavior 
# (notably that Word('foo') == Word('bar') would evaluate to true). 
# It wouldn't make sense to test for equality based on length, so 
# we fall back on str's implementation of equality.

# Now would be a good time to note that you don't have to define 
# every comparison magic method to get rich comparisons. 
# The standard library has kindly provided us with a class 
# decorator in the module functools that will define all 
# rich comparison methods if you only define __eq__ and 
# one other (e.g. __gt__, __lt__, etc.) This feature is 
# only available in Python 2.7, but when you get a chance 
# it saves a great deal of time and effort. You can use it by 
# placing @total_ordering above your class definition.

class Word(str):
    def __new__(cls, word):
        return str.__new__(cls, word.lstrip(" ").rstrip(" "))

    def __cmp__(self, other):
        return 

    def __gt__(self, other):
        return len(self) > len(other.lstrip(" ").rstrip(" "))

    def __lt__(self, other):
        return len(self) < len(other.lstrip(" ").rstrip(" "))

    def __ge__(self, other):
        return len(self) >= len(other.lstrip(" ").rstrip(" "))

    def __le__(self, other):
        return len(self) <= len(other.lstrip(" ").rstrip(" "))

w = Word(" Tes ")
# Using different magic methods below:

# Greater than __gt__
print(w > " Test ")
# Less than __lt__
print(w < " Test ")
# Greater than equal to __ge__
print(w >= " Test ")
# Less than equal to __gt__
print(w <= " Test ")
