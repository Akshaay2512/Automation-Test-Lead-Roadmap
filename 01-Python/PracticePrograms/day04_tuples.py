#Example 1  Creating tuple

mytuple1 = ("apple", "banana", "cherry")
print(mytuple1)

print( "=" * 20)

#Example 2  access the tuple

mytuple2 = ("apple", "banana", "cherry")
print(mytuple2[1])

print( "=" * 20)

#Example 3 range of indexes

mytuple3 = ("apple", "banana", "cherry", "oranage", "kiwi", "melon", "mango")
print(mytuple3[2:5])
print(mytuple3[-4:-1])

print( "=" * 20)

#Example 4 change tuple items
# by default we can not do but option is convert tuple as list > update and again change back to tuple

mytuple4 = ("apple", "banana", "cherry")
mylist1=list(mytuple4)
mylist1[0] = "orange"

mytuple4 = tuple(mylist1)
print(mytuple4)

#Example 5 Reading tuple items using loop

mytuple5 = ("apple", "banana", "cherry")

for i in mytuple5:
    print(i)

#Example 6 Searching item in tuple

mytuple6 = ("apple", "banana", "cherry")

if "apple" in mytuple6:
    print("Yes")
else:
    print("No")

# Example 7 total item available
mytuple7 = ("apple", "banana", "cherry", "oranage", "kiwi", "melon", "mango")
print(len(mytuple7))

# Example 8 add items in tuple (negative case)

# mytuple8 = ("apple", "banana", "cherry", "oranage", "kiwi", "melon", "mango")
# mytuple8[1] = "Berry"
#
# print(mytuple8)

# Example 9 copying tuple

mytuple9 = ("apple", "banana", "cherry", "oranage", "kiwi", "melon", "mango")

mytuple10 = mytuple9
print(mytuple10)

# Example 10 Removing item from tuple (negative case)

# mytuple11 = ("apple", "banana", "cherry", "oranage", "kiwi", "melon", "mango")
# del mytuple11
# # mytuple11.remove("apple")
# print(mytuple11)

# Example 11 combine/join tuple

mytuple12 = ("apple", "banana", "cherry", "oranage", "kiwi", "melon", "mango")
mytuple13 = (1,2,3,4,5)

mytuple14 = mytuple12 + mytuple13

print(mytuple14)


# Example 11 tuples are equal or not
mytuple12 = ("apple", "banana", "cherry", "oranage", "kiwi", "melon", "mango")
mytuple13 = (1,2,3,4,5)

if mytuple12 == mytuple13:
    print("Yes")
else:
    print("No")
