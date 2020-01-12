# HEAD
# Data Static Class method usage
# DESCRIPTION
# Describes the usage of static classes and methods
# RESOURCES
# 
# https://dzone.com/articles/definitive-guide-how-use

# Static methods in classes are used 
#       without instantiation
# They are independant methods clubbed into classes
# Purposes can be isolation, modularization, etc
class Arithmatic:
    def sum(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum
    def diff(self, *args):
        diff = 0
        for i in args:
            diff -= i
        return diff
    def mul(self, *args):
        mul = 1
        for i in args:
            mul *= i
        return mul
    def div(self, *args):
        div = 1
        for i in args:
            div /= i
        return div

total = Arithmatic.sum(1,2,3,4,5)
print("Sum", total)
total = Arithmatic.diff(15,10,5,4,3,2)
print("Diff", total)
total = Arithmatic.mul(1,2,3,4,5)
print("Mul", total)
total = Arithmatic.div(15,3,2,1)
print("Div", total)
