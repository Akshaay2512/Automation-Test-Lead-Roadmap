#Method 1:
a = 25
b = 40

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)

#method 2:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)

#Method 3:
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print("Largest number is:", largest(25, 40))

#Method 4:
a = 25
b = 40

print("Largest number is:", max(a, b))

#Method 5: if two numbers equal
a = 40
b = 40

if a > b:
    print("Largest number is:", a)
elif b > a:
    print("Largest number is:", b)
else:
    print("Both numbers are equal")

# Q1. Which is the simplest way to find the largest of two numbers?
# Answer: Using the max() function.
#
# Q2. Which method is commonly asked in interviews?
# Answer: Using the if-else statement.