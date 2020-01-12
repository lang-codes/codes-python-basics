# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes how a variable copying works
# RESOURCES
# 

spam = 42
# Copying not referencing
cheese = spam
print(cheese)
# 42
spam = 100
print(spam)
# 100
print(cheese)
# 42
