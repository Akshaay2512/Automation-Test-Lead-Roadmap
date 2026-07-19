#conditional statement
# if if.else elif
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be

#Example 1: print personal eligible for vote
#age>=18

age = 15
if age >= 18:
    print("YOU CAN VOTE since your age is:", age)

else:
    print("NOT ELIGIBLE FOR VOTE since your age is:", age)


#Example 2

if True:
    print("Condition is true")
else:
    print("Condition is false")

#Example 3

if 0:
    print("One")
else:
    print("Not one")

#Example 4

number = 10

if number%2==0:
    print("EVEN")
else:
    print("FALSE")

#Example 5 Ternary operator

num=9
print("Even number") if num%2==0 else print("Odd")

#Example 6: if else
a=1

if a>=10:
    print("Hello", "Python")
else:
    print("Not", "Today")

#also can be written with {} if more than one statement [Ternary operator]

{print("hello boss"), print("Welcome")} if a>=10 else {print("DONT"), print("COME")}

#Example 6: elif

week=4
if week==1:
    print("Sunday")
elif week==2:
    print("Monday")
elif week==3:
    print("Tuesday")
else:
    print("Invalid")