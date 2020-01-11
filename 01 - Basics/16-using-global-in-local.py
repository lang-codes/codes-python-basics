# Describe usage of 'global' key

# 'global' key is used to reference a variable 
#       usage or definition in global context 
#       within a local scope; whichever applies


def spam():
    global var
    print(var)
    # Linter Complains of "Using variable 'var' before assignment"
    # but code works
    var = 'spam'


var = 'global'
spam()
print(var)
