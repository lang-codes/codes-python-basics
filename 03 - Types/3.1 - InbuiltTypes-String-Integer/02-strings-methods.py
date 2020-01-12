# HEAD
# DataType - String Methods
# DESCRIPTION
# Describes string manipulation, methods available, 
#       and it details
# RESOURCES
# 

# len() is an inbuilt function that gives the number of characters in a string
#       since string behaves like a iterator

name = "     I am a string which is a list of characters joined together     "

# length of string list OR number of characters
print("len", len(name))

# Capitalize string
print("capitalize", name.capitalize())

# String to lowercase
print("lower", name.lower())

# String to uppercase
print("upper", name.upper())

# Make string caseless for comparision
print("casefold", name.casefold() == name.upper().casefold())

# Count the number of characters
print("count", name.count('s',0,len(name)))

# Encode a string value to a different encoding
# 'strict' or 'ignore' or 'replace' alternate errors value
print("encode", name.encode(encoding="utf8", errors="strict"))

# Find a character or phrase
print("find", name.find("s", 0, len(name)))

# Return the index of the first matching item
print("index", name.index("s"))

# Checks if string is numeric
print("isnumeric", name.isnumeric())

# Checks if string are all alphabets
print("isalpha", name.isalpha())

# Checks if string is alpha numeric
print("isalnum", name.isalnum())

# Checks if string is a decimal
print("isdecimal", name.isdecimal())

# Checks if string is a digit
print("isdigit", name.isdigit())

# Checks if string is a valid identifier according to language
print("isidentifier", name.isidentifier())

# Checks if string is upper case
print("islower", name.islower())

# Checks if string is lower case
print("isupper", name.isupper())

# Checks if string is title cased - capitalized first character of word
print("istitle", name.istitle())

# Checks if all characters are whitespace
print("isspace", name.isspace())

# Checks if printable
# if empty space then false
print("isprintable", name.isprintable())

# Split using provided delimiter
# maxsplit mentioned is optional and default is all
#   else splits based the number of counts
print("split", name.split("s", maxsplit=-1))

# Join function joins all the iterable items into a string
print("join", name.join(name.split("string", maxsplit=-1)))

# Removes characters
# Strip of leading white spaces
print("lstrip", name.lstrip())

# count is optional and if not provided will remove all
# print(name.replace(old, new, count))
print("replace", name.replace("string", "s.t.r.i.n.g", -1))

# returns highest index if there are a number of string words
# start (2nd arg) and end (3rd arg) are optional
print("rfind", name.rfind("s", 0, len(name)))

# returns highest index if there are a number of string words
# start (2nd arg) and end (3rd arg) are optional
# Raises error if substring not found
print("rindex", name.rindex("s"))

# Removes characters
# Strip of trailing white spaces
print("rstrip", name.rstrip("string"))
