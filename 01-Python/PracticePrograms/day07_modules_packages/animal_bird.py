# Calling function from animal and bird file

#Approach 1:

import animal
import bird

animal.fly()
animal.color()

bird.fly()
bird.color()

print("==" * 20, "Approach 2 ", "==" * 20)

#Approach 2:

from animal import *
fly()
color()
from bird import *
fly()
color()

