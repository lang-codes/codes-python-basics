# Describes usage of sort with both 
#       options of 'key' function and 'reverse' boolean

spam = ['A', 'a', 'z', 'A', 'Z']
# key is a function
spam.sort(key=None, reverse=False)
print(spam)
# RESULT:
# ['a', 'A', 'z', 'Z']

# key is a function
# Pass function without invocation
spam.sort(key=str.upper, reverse=False)
print(spam)
# RESULT:
# ['a', 'A', 'z', 'Z']

spam = [1,22222,33,44444444,5123]
# key is a function
# Pass function without invocation
spam.sort(key=int.bit_length, reverse=False)
print(spam)
# RESULT:
