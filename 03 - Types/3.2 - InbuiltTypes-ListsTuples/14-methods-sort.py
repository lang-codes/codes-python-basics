# HEAD
# DataType - List method - sort()
# DESCRIPTION
# Describes using sort on list based 
#       of only integers or only alphabets
# RESOURCES
# 

lists = [2, 5, 3.14, 1, -7]

# USAGE
# Simple sort function on integer list without specifications
lists.sort()
print(lists)
# Results in following
# [-7, 1, 2, 3.14, 5]

lists = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
# Simple sort function on alphabet list without specifications
lists.sort()
print(lists)
# RESULT:
# ['ants', 'badgers', 'cats', 'dogs', 'elephants']

# Simple sort function on alphabet list 
#       with reversing specifications
lists.sort(reverse=True)
print(lists)
# ['elephants', 'dogs', 'cats', 'badgers', 'ants']