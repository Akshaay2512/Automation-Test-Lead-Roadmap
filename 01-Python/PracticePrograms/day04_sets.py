# Example 1 Creating set

myset1 = {"apple","bannana", "Cherry", "orange", "lemon", "kiwi"}
print(myset1)

#Example 2: Accessing items from set

myset2 = {"apple","bannana", "Cherry", "orange", "lemon", "kiwi"}
for i in myset2:
    print(i)

#Example 3: values exists in set or not

myset3 = {"apple","bannana", "Cherry", "orange", "lemon", "kiwi"}

print("apple" in myset3)
print("car" in myset3)

#Example 4: Adding items to set
# add = addition of single item
# update = addition of multiple items

myset4 = {"apple","bannana", "Cherry", "orange", "lemon", "kiwi"}
myset4.add("dates")
print(myset4)
myset4.update(["Tomato", "berry"])
print(myset4)

#Example 5: find number of items (len)

myset5 = {"apple","bannana", "Cherry", "orange", "lemon", "kiwi"}
print(len(myset5))

#Example 6: Remove items from set
# remove()
#discard()

myset6 = {"apple","bannana", "Cherry", "orange", "lemon", "kiwi"}

myset6.remove("apple")
print(myset6)

# myset6.remove("xyz")
# print(myset6)  #negative case(will throw error if item not available)

myset6.discard("Cherry")
print(myset6)

myset6.discard("xyz")
print(myset6)  #negative case(will not throw error if item not available)

#Example 7: Clear all items from set

myset7 = {"apple","banana", "Cherry", "orange", "lemon", "kiwi"}
myset7.clear()
print(myset7) # still set is available only items will be removed

# del myset7
# print(myset7) # completely delete the set and items

#Example 8: Join 2 sets

myset8 = {"apple","banana", "Cherry", "orange", "lemon", "kiwi"}
myset9 = {1,2,3}

myset10 = myset8.union(myset9)
print(myset10)

#update()
myset11 = {"apple","banana", "Cherry", "orange", "lemon", "kiwi"}
myset12 = {1,2,3}
myset11.update(myset12)
print(myset11)

#Example 9: Remove duplicates from list

numbers=[1,2,2,3,4,4,5]

print(list(set(numbers)))

