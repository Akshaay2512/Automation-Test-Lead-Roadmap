#break and continue

for i in range (1,10):
    if i==5:
        break
    print(i)
print("Program exited!!")

#continue

for i in range (1,10):
    if i==5 or i==3 or i==4:
        continue
    print(i)
print("Program exited!!")

#range three

for i in range (3,7,2):
    print(i)