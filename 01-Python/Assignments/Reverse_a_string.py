#Reverse string (interview question)

#Method 1 looping

m="Akshaay"
n=""

for i in m:
    n=i+n

print("Reverse value is:", n)


#Method 2 using slicing operator
k="Akshaay Kiran"
l=k[::-1]
print(l)