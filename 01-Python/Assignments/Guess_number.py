import random

from docutils.io import Input

secret_number = random.randint(1,10)

guess = int(input("Enter the number: "))

if guess > secret_number:
    print("Too high")
elif guess < secret_number:
    print("Too low")
else:
    print("CORRECT")

print(f"The secret number was {secret_number}")

