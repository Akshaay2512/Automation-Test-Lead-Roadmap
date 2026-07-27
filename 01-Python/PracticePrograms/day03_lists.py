#Example 1 : Create list

mylist1 =[10,20,30,40,60]
mylist2 =["apple","bannana", "Cherry"]
mylist3 =["apple", 10, "banana", 20]
mylist4 =list()

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist4)

print("=" * 20)

#Example 2 : Accessing items from the list

mylist = ["apple","bannana", "Cherry"]  #[0, 1, 2] or [-3, -2, -1]

print(mylist[-1])
print(mylist[1])

print("=" * 20)


#Example 3 : Range of indexes

mylist5 = ["apple","bannana", "Cherry", "orange"]
print(mylist5[1:3])
print(mylist5[-2:-1])

print("=" * 20)

#Example 4: Change item values from list

mylist6 = ["apple","bannana", "Cherry", "orange", "lemon", "kiwi"]
print(mylist6)

mylist6[1] = "mango"
print(mylist6)

print("=" * 20)

#Example 5: Read the items in list from loop statement

mylist7 = ["apple","bannana", "Cherry", "orange", "lemon", "kiwi"]

for i in mylist7:
    print(i)

print("=" * 20)

#Example 6: Check if item exists in list or not

mylist8 = ["apple","bannana", "Cherry", "orange", "lemon", "kiwi"]

if "apple" in mylist8:
    print("Is available")
else:
    print("Not available")

print("=" * 20)

#Example 7: Total number if items in list

mylist9 = ["apple","bannana", "Cherry", "orange", "lemon", "kiwi"]

print(len(mylist9))

print("=" * 20)

#Example 8: Add new item in list inset() or append()
mylist10 = ["apple","bannana", "Cherry", "orange", "lemon", "kiwi"]
mylist10.append("dates")
print(mylist10)

mylist10.insert(3,"berry")
print(mylist10)
print(mylist10.index("Cherry"))

print("=" * 20)

#Example 9: Remove item from list pop(), del(), clear()

#pop()
mylist11 = ["apple","bannana", "Cherry", "orange", "lemon", "kiwi"]
print(mylist11)
mylist11.pop(2)
print(mylist11)

#del
del mylist11[1]
print(mylist11)

#clear
mylist11.clear()
print(mylist11)

#Example 10: Copy from one list to another

#Method 1
mylist12 = ["apple","bannana", "Cherry", "orange", "lemon", "kiwi"]
mylist13=list(mylist12)

print(mylist12)
print(mylist13)

print("=" * 20)

#Method 2:
mylist13=mylist12.copy()
print(mylist13)

print("=" * 20)

#Example 11: Combine/join list

# String operator method
lista=["a", "b", "c"]
listb=[1, 2, 3]

listc=lista+listb
print(listc)

#Looping statement method

listd=["a", "b", "c"]
liste=[1, 2, 3]

for i in liste:
    listd.append(i)

print("Combined list: ", listd)

#Extend method - extend()

listf=["a", "b", "c"]
listg=[1, 2, 3]
listf.extend(listg)
print(listf)
