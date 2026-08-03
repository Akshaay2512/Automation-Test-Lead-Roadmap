# Method 1: for loop

a = 1
b = []

for i in range(1,101,1):  #(start, stop, step(increase/decrease)
    print(i)

# Method 2:
i = 1

while i <= 100:
    print(i)
    i += 1

#Method 3:

def print_numbers():

    for i in range(1, 101):
        print(i)

print_numbers()

# 1 to 10
range(1, 11)

# 1 to 100
range(1, 101)

# Even numbers from 2 to 20
range(2, 21, 2)

# Odd numbers from 1 to 19
range(1, 20, 2)

# Reverse from 10 to 1
range(10, 0, -1)