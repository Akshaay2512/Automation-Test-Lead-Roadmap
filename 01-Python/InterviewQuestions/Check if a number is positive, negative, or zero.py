#Method 1: IF

num = -10

if num > 0:
    print(num, "is Positive")
elif num < 0:
    print(num, "is Negative")
else:
    print("The number is Zero")

#Method 2: input from user

num = int(input("Enter a number: "))

if num > 0:
    print(num, "is Positive")
elif num < 0:
    print(num, "is Negative")
else:
    print("The number is Zero")

#Method 3: using function

def check_number(num):

    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-10))

#Method 4: Nested if

num = 15

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")