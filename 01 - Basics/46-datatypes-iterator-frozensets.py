# HEAD
# Python Basics - Frozen Sets Data Types
# DESCRIPTION
# Describes how
#       - frozenset (immutable set) is created using frozenset
#
# RESOURCES
#


# # NON-SEQUENCE ITERATORS
# Sequence based Iterators allow identification or reference
#       of every loop-able item with an KEY or NO REFERENCE/KEY/INDEX

# # # FROZENSET
# Frozensets are sets which are immutable
# Frozensets are sets with no reference of item like Index or Key
#       with round bracket in definitions
# Frozensets can only have unique items
# Value can be of any type


# FROZENSET can have any unique (mixed) value as item
var = frozenset({1, "s"})

# Using frozenset function to create a FROZENSET
# FROZENSET cannot have duplicates
var = frozenset({1, "s"})

var = frozenset({"name", []})

var = frozenset({"name", [1, 2]})

var = frozenset({1, [1, 2], 1})

var = frozenset({"s", [1, 2], 1, 1, 2})
# Results in {"s", [1, 2], 1, 2}
