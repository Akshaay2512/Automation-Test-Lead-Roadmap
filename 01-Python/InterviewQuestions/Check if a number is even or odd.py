#Method 1: IF

num = 25

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

#Method 2: Getting input from user:
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

#Method 3: Function

def even_odd(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(25))

#Method 4: Ternary operator

num = 18

result = "Even" if num % 2 == 0 else "Odd"

print(result)

#Method 5: using %

num = 18

if num & 1:
    print("Odd")
else:
    print("Even")

# Q1. How do you check whether a number is even or odd?
#
# Answer: By checking the remainder when the number is divided by 2 using the modulus (%) operator.
#
# Q2. Which operator is used to check even or odd?
#
# Answer: The modulus (%) operator.
#
# Q3. Why do we use num % 2 == 0?
#
# Answer: If the remainder is 0, the number is even; otherwise, it is odd.
#
# Q4. Which method is preferred in interviews?
#
# Answer: The if-else method because it clearly demonstrates the logic.