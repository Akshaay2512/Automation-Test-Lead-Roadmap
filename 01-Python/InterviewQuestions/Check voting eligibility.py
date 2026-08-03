#Method 1: if

age = 17

if age >= 18:
    print(f"Your age is {age}, so you are eligible to vote.")
else:
    print(f"Your age is {age}, so you are not eligible to vote.")

#Method 2: getting user input

age = int(input("Enter the age:"))

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

#Method 3: using function

def check_age(age):

    if age >= 18:
        return f"Your age is {age}, so you are eligible to vote."
    else:
        return f"Your age is {age}, so you are not eligible to vote."

print(check_age(11))

#Method 4: Ternary operator

age = 16

result = "Eligible to Vote" if age >= 18 else "Not Eligible to Vote"

print(result)