# Describes multiple returns from functions returned as tuple 

def square(x,y):
    return x*x, y*y

t = square(2,3)
print(t)  # Produces (4,9)
# Now access the tuple with usual operations

def squareTwo(x,y):
    return x*x, y*y

xsq, ysq = squareTwo(2,3)
print(xsq)  # Prints 4
print(ysq)  # Prints 9  
# Tuple has vanished!