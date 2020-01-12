# HEAD
# DataType - String Introduction
# DESCRIPTION
# Describes what is a string and it details
# RESOURCES
# 

# Strings can be assigned to a variable
# Strings are list of character joined together
# Strings can be referenced using indexes and indexing starts from 0/Zero
# String's characters cannot be changed or mutated inplace
# The whole string value has to be reassigned to the variable

name = "I am a string which is a list of characters joined together"

# Print string
print(name)
print(type(name))

# Type Conversion blank string
typeConversion = bool("")
print("typeConversion", typeConversion)

# Type Conversion string
typeConversion = bool("I hate cybercrime")
print("typeConversion", typeConversion)

# Access string character using index of the character
print("First character", name[0])
print("Last character", name[len(name)-1])

