# HEAD
# Classes Abstract Classes
# DESCRIPTION
# Describes multiple returns from functions returned as tuple 
# Also referred to as destructuring
# RESOURCES
# 

def square(x,y):
    # return (x*x, y*y)
    # Following line is equivalent to above line
    return x*x, y*y

t = square(2,3)
print(t)  # Produces a tuple - (4,9)
# Now access the tuple with usual operations

def squareTwo(x,y):
    # return (x*x, y*y)
    # Following line is equivalent to above line
    return x*x, y*y

xsq, ysq = squareTwo(2,3)
# Tuple has vanished! 
# Well, not really they were DESTRUCTURED to different variables
print(xsq)  # Prints 4
print(ysq)  # Prints 9  

