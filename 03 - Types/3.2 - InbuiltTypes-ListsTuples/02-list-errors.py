# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes errors of indexing when not inside the range
# RESOURCES
# 

lists = ['cat', 'bat', 'rat', 'elephant']
lists[10000]

# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
    # lists[10000]
# IndexError: list index out of range

lists[int(1.0)]

# Following throws error (Uncomment & check)
# lists[1.0]

# ERROR DETAILS - 
# Traceback (most recent call last):
#   File "<pyshell#13>", line 1, in <module>
    # lists[1.0]
# TypeError: list indices must be integers, not float
