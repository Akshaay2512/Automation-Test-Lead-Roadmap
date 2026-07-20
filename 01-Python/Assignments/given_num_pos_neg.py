# Check the given number is positive or negative
# Print week number if you provide weekname as input

#Check the given number is positive or negative

number = int(input("Enter the number: "))

if number > 0:
    print(f"{number} is Positive number")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is Zero")