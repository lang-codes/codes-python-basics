# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes tuple as a immutable object - TypeError
# RESOURCES
# 

eggs = ('hello', 42, 0.5)
eggs[1] = 'immutability test'

# Traceback (most recent call last):
#   File "45-tuples-error.py", line 2, in <module>
#     eggs[1] = 'immutability test'
# TypeError: 'tuple' object does not support item assignment