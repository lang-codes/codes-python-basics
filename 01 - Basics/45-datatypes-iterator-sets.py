# HEAD
# Python Basics - Sets Data Types
# DESCRIPTION
# Describes how
#       - sets are created
#       - set function is used to create a set
#
# RESOURCES
#


# # NON-SEQUENCE ITERATORS
# Sequence based Iterators allow identification or reference
#       of every loop-able item with an KEY or NO REFERENCE/KEY/INDEX

# # # SETS
# Sets are like lists with no reference of item like Index or Key
#       with round bracket in definitions
# Sets can only have unique items
# Value can be of any type

# SET can have any unique (mixed) value as item
var = {1, "s"}

# SET can have any unique value as item
var = {1, "s"}

var = {"name", []}

# Using set function to create a SET
var = set({"name", [1, 2]})

# Using set function to create a SET
# SET cannot have duplicates
var = set({1, [1, 2], 1})

# SET cannot have duplicate items
var = set({"s", [1, 2], 1, 1, 2})
# Results in {"s", [1, 2], 1, 2}
