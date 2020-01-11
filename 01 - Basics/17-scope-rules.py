# Describes scope rules in terms of local and global

# Assignation of variables inside a local 
#       scope makes the variable locally scoped, 
#       even if a global variable is available 
#       in the global scope
# Refer global variables with 'global' key
# Once referred as global with 'global' key, it can 
#       be referred

def spam():
    global var
    var = 'spam'  # this is the global


def bacon():
    var = 'bacon'  # this is a local


def ham():
    print(var)  # this is the global since there is no assignment


var = 42  # this is the global
spam()
print(var)  # prints spam since is global
bacon()
print(var)
# prints spam since bacon implements local 
#       variable and doesnt effect var variable
