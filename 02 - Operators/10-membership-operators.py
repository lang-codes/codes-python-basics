# Describe the usage of membership operators

# 'in' operator checks if an item is a part of 
#       a sequence or iterator
# 'not in' operator checks if an item is not 
#       a part of a sequence or iterator

lists = [1, 2, 3, 4, 5]
dictions = {"key": "value", "a": "b", "c": "d"}

# Usage with lists for
# 'not in' AND 'in'

# 'in' checks for item in sequence
if (1 in lists):
    print("in operator - 1 in lists:", (1 in lists))

# 'in' checks for absence of item in sequence
if (1 not in lists):
    print("not in operator - 1 not in lists:", (1 not in lists))

# 'in' checks for absence of item in sequence
if ("b" not in lists):
    print("not in operator - 'b' not in lists:", ("b" not in lists))

# Usage with dictions for
# 'not in' AND 'in'

# 'in' checks for item in sequence
# diction.keys() return a sequence
if ("key" in dictions.keys()):
    print("in operator - 'key' in dictions.keys():", ("key" in dictions.keys()))

# 'not in' checks for absence of item in sequence
# diction.keys() return a sequence
if ("key" not in dictions.keys()):
    print("not in operator - 'key' in dictions.keys():",
          ("key" not in dictions.keys()))

if ("somekey" not in dictions.keys()):
    print("not in operator - 'somekey' in dictions.keys():",
          ("somekey" not in dictions.keys()))
