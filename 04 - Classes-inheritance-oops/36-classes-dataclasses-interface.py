# HEAD
# Data Class Annotation - @dataclass
# DESCRIPTION
# Describe the 
# RESOURCES
# 

# https://stackoverflow.com/questions/35988/c-like-structures-in-python

from dataclasses import dataclass

@dataclass
class DataPoint:
    x: float
    y: float
    z: float = 0.0

p = DataPoint(1.5, 2.5)
# DataPoint(x=1.5, y=2.5, z=0.0)
print(p)  

p = DataPoint(1.5, 2.5, 3.5)
# DataPoint(x=1.5, y=2.5, z=3.5)
print(p)  
