# Describes how strings are immutable
# String cannot be manipulated or reassigned in place
# Only a new entire string value can be re-assigned to a variable

name = 'Zophie a cat'
name[7] = 'the'

# Traceback (most recent call last):
#   File "<pyshell#50>", line 1, in <module>
    # name[7] = 'the'
# TypeError: 'str' object does not support item assignment