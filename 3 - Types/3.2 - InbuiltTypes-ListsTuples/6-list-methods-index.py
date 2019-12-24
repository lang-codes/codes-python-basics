# Describes index method of lists

lists = ['hello', 'hi', 'howdy', 'heyas']
# .index(item) gives access to index of an item
# returns the first occurance item
print(lists.index('hello'))

listsmer = ['hello', 'hi', 'howdy', 'heyas', 'hello']

# returns the first occurance item even if two are there
print(listsmer.index('hello'))
