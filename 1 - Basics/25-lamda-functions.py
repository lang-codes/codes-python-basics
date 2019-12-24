# Describes creation and usage of lamda functions
# Lamda functions can be simple lamda or nested lamda functions

# LAMBDA FUNCTION

# Python supports the creation of lamda or anonymous functions
# (i.e. functions that are not bound to a name) at runtime,
# using a construct called lambda.
# This is not same as lambda in functional programming,
#       but a concept well integrated 
#       into Python and used in conjunction
# with typical functional concepts like 
#       filter(), map() and reduce()

# Like def keyword, lambda creates a function to be called later.
# But it returns the function instead of assigning it to a name

# USAGE
# lambda arg1, arg2, ...argN : expression using arguments
# lambda is an expression, not a statement
# lambda's body is a single expression, not a block of statements.
# def f(x, y, z): return x + y + z
# lambda x, y, z: x + y + z


def lamb(x): return x ** 3


print(lamb(5))

# allows us to embed a function within the code
# For instance, callback handlers are frequently coded as
# inline lambda expressions embedded directly 
#       in a registration call's arguments list
L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]
for f in L:
    print(f(3))

# NESTED LAMBDA
# the lambda appears inside a def and so can 
#       access the value that
# the name x has in the function's scope at 
#       the time that the enclosing function was called


def action(x):
    # Make and return function, remember x
    return (lambda newx: x + newx)


# lambda also has access to the names in any enclosing lambda
action = (lambda x: (lambda newx: x + newx))
ans = action(99)
