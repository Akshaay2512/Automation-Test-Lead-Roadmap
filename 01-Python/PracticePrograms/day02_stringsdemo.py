#creating strings empty

#Example 1
name =""
name=''
name=str()

#mutable - cannot change the value of the variable
#immutavle - can change the value of the variable

print("=" * 30)

#Example 3
# strings are immutable

str1 = "welcome"
print(id(str1)) #ID1

str1=str1+"to python"
print(id(str1)) #ID2   #It is immutable since two different IDs generated

print("=" * 30)

#Example 3: Use of operator

str = "Welcome"
print(str+"programming")

print(str*2) # print string value multiple time

print("=" * 30)

#Example 4: slicing operator

str2 = "Welcome"

print(str2[1:3])
print(str2[:6])
print(str2[2:])

print(str2[1:-1])
print(str2[1:-2])
print(str2[1:-2])

print("=" * 30)


#Example 5: ord() and chr()

print(ord("a"))
print(chr(97))

print("=" * 30)

#Example 6: max() and min() and len()

print(max("Akshaay"))
print(min("Akshaay"))
print(len("Akshaay"))

print("=" * 30)

#Example 7: in,  not in operators - return True or False

s= "welcome"

print("come" in s)
print("lome" in s)

print("come" not in s)
print("lcome" not in s)

print("=" * 30)

#Example 8: string comparison

print("tim" == "tee")
print("free" != "freedom")

print("=" * 30)

#Example 9: testing strings - Returns True or False

s = "Welcome to Python"

print(s.isalnum())
print("welcome".isalpha())
print("1234".isdigit())
print("First numner".isidentifier())
print(s.islower())
print("WELCOME".isupper())
print("WelCome".isupper())
print("Welcome Python".isspace())

#Example 10: testing strings - Searching for substrings

y="Welcome to India"

check = y.endswith("dia")
print(check)

if check == True:
    print("OMG I DID!!!")

if y.startswith("Wel"):
    print("Again I DID!!")
else:
    print("Better luck")

if y.find("zzz") != -1:
    print("Boss mode")
else:
    print("Not a boss")

print(y.count("a"))

print(len("Welcome"))

#Example 11: converting string

z= ("string in Python")

z1=print(z.capitalize())
z2=print(z.title())
z3=print(z.lower())
z4=print(z.upper())
z5=print(z.swapcase())
z6=print(z.replace("in","on"))

#Example 12: Reverse string (interview question)

#Method 1 looping

m="Akshaay Kiran"
n=""

for i in m:
    n=i+n

print("Reverse value is:", n)

#Method 2 using slicing operator
k="Akshaay Kiran"
l=k[::-1]
print(l)





