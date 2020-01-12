# HEAD
# DataType - List method - append() Usage Errors
# DESCRIPTION
# Describes type of error when method 
#       of list or one type used on another
# RESOURCES
# 

foo = 'hello'

# Though strings work like lists/sequences, they are
#       are immutable and items of group of items cannot 
#       be added to string data type
# Uncomment & check error
# foo.append('world')

# ERROR DETAILS - 
# Traceback (most recent call last):
#   File "<pyshell#19>", line 1, in <module>
    # foo.append('world')
# AttributeError: 'str' object has no attribute 'append'
