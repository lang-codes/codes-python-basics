# Describes how strings are immutable

# String cannot be manipulated or reassigned in place
# Only a new entire string value can be re-assigned to a variable

name = 'Zophie a cat'

# Cannot modify string characters
# The whole string value has to be reassigned
# UNCOMMENT the following and check error

# name[7] = 'the'

# Traceback (most recent call last):
#   File "<pyshell#50>", line 1, in <module>
    # name[7] = 'the'
# TypeError: 'str' object does not support item assignment

# This works
name = 'Zophie the cat'
