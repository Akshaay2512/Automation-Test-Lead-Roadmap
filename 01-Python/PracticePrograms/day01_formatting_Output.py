name,age,sal = "John", 30, 5000.22

# Approach 1
print(name,age,sal)

#Approach 2
# print("Name is:", name)
# print("Age is:", age)
# print("Salary is:", sal)

#Approach 3
# print("Name is:%s Age is%d Salary is:%g" %(name,age,sal))

#Approach 4
print("Name is:{} Age is:{} Salary is:{}" .format(name,age,sal))
print("Age is:{} name is:{} Salary is:{}" .format(age,name,sal)) # order of variables is important