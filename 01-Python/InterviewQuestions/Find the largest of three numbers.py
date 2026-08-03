#Method 1:
a = 25
b = 40
c = 35

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

#Method 2:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

#Method 3:
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Largest number is:", largest(25, 40, 35))

#Method 4:
a = 25
b = 40
c = 35

print("Largest number is:", max(a, b, c))

# Q1. Which method is most commonly asked in interviews?
#
# Answer: Using if-elif-else conditions.
#
# Q2. Which built-in function can find the largest number?
#
# Answer: max().
#
# Q3. Why do we use >= instead of >?
#
# Answer: To correctly handle cases where two or more numbers are equal.
#
# Q4. What is the time complexity of this program?
#
# Answer: O(1) because it performs a fixed number of comparisons regardless of the input values.

