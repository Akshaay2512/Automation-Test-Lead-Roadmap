# calling function from calculator file

#approach 1:

import calculator
calculator.add(1,2)
calculator.mul(22,10)

#approach 2:

from calculator import add, mul
add(11,22)
mul(22,1)

#Approach 3:

from calculator import * # determines all the methods available
add(1,2)
mul(2,2)
