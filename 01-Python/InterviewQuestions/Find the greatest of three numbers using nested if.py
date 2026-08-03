#Method 1: nested if

a = 60
b = 100
c = 99

if a > b:
    if a > c:
        print(f"A {a} is greater")
    else:
        print(f"C {c} is greater")

else:
    if b > c:
        print(f"B {b} is greater")
    else:
        print(f"c {c} is greater")

#Method 2: Getting user input:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("Greatest number is:", a)
    else:
        print("Greatest number is:", c)
else:
    if b > c:
        print("Greatest number is:", b)
    else:
        print("Greatest number is:", c)

#Method 3: Using function

def greater(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print(greater(10,5,2))