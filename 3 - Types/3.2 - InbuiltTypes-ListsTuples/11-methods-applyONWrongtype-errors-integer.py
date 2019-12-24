# Describes type of error when method of list or one type used on another

bacon = 42
bacon.insert(1, 'world')

# ERROR DETAILS - 
# Traceback (most recent call last):
#   File "<pyshell#22>", line 1, in <module>
    # bacon.insert(1, 'world')
# AttributeError: 'int' object has no attribute 'insert'
