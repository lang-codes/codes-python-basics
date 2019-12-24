# Describes usage of for loop

# for loop can iterate over sequence or sequence like objects
# range() is an inbuilt function that returns 
#       results over time during iteration
# range() returned a sequence in py2.x

# USAGE
# for item in iterator:
#   execution block

# for item in range(int):
#   execution block

# Variations of range:
# range(int)
# range(start, stop)
# range(start, stop, increment)

for i in range(5):
    print('Will print five times ' + str(i))
for i in range(2, 6):
    print('Will print six times using start and finish - will include 1st and exclude last ' + str(i))
for i in range(0, 6, 1):
    print('Will print two times using number of increments in the last ' + str(i))

list = [2, 3, 4, 5, 6, 7, 8]

for idx, item in enumerate(list):
    print(item, idx)
