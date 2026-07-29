#Example 1: Create dictionary

mydic1 = {101:"x", 102:"y", 103:"z"}
print(mydic1)

print("===" * 20)

#Example 2: accessing items from dictionary

mydic2 = {
        "brand" : "Ford",
        "model" : "ikon",
        "year"  : 2025
}
print(mydic2["brand"])
print(mydic2["year"])

#using get function

print(mydic2.get("brand"))
print(mydic2.get("model"))

print("===" * 20)

#Example 3: Change values from dictionary

mydic3 = {
        "brand" : "Ford",
        "model" : "ikon",
        "year"  : 2025
}
print(mydic3)

mydic3["year"] = 2026  #change value
print(mydic3)

print("===" * 20)

#Example 4: reading values from dictionary using loop

mydic4 = {
        "brand" : "Ford",
        "model" : "ikon",
        "year"  : 2025
}

for i in mydic4:
    print(i) # prints only keys from dictionary

print("===" * 20)

for i in mydic4:
    print(mydic4[i]) # prints only values from dictionary

print("===" * 20)

for i in mydic4.values():
    print(i)          # prints only values from dictionary

print("===" * 20)

for x,y in mydic4.items():
    print(x,y)           # prints keys and  values from dictionary

print("===" * 20)

#Example 5: Check if key exists in dictionary or not

mydic5 = {
        "brand" : "Ford",
        "model" : "ikon",
        "year"  : 2025
}

if "model" in mydic5:
    print("yes")
else:
    print("No")

print("===" * 20)

# True or false method

print("model" in mydic5)
print("data" in mydic5)

print("===" * 20)

#Example 6: Find number of items in dictionary

mydic6 = {
        "brand" : "Ford",
        "model" : "ikon",
        "year"  : 2025
}

print(len(mydic6))

print("===" * 20)

#Example 7: Add items to dictionary

mydic7 = {
        "brand" : "Ford",
        "model" : "ikon",
        "year"  : 2025
}

mydic7["color"] = "Red"
print(mydic7)

print("===" * 20)

#Example 8: Remove items from dictionary

mydic8 = {
        "brand" : "Ford",
        "model" : "ikon",
        "year"  : 2025
}

mydic8.pop("year")
print(mydic8)

del mydic8["model"]
print(mydic8)

mydic8.clear()
print(mydic8)

print("===" * 20)

#Example 9: copy items from dictionary

mydic9 = {
        "brand" : "Ford",
        "model" : "ikon",
        "year"  : 2025
}

mydic10 = mydic9
print(mydic10)

mydic11= mydic9.copy()
print(mydic11)
