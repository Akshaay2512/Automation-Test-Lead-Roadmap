## Method and constructor

# Method: we can give any name
#         method return value
#         method can take arg/parameters
#         we have to use an obj to invoke the method

# Constructor: Name is fixed: __init__(self):
#                 constructor will not return any value
#                 constructor also take arg/parameters
#                 constructor will be called at the time of obj creation itself

#Example 1:
class myclass1():
    def __init__(self):
        print("This is constructor")
    def m1(self):
        print("hello")

mc1=myclass1()  # calling method directly from class

# Example 2:

class myclass2():
    def __init__(self):
        print("this is cons")
    def m1(self):
        print("hello")
    def m2(self,x,y):
        return (x+y)

mc = myclass2()  # invoke constructor automatically
mc.m1() # Method we have to call by using object
print(mc.m2(10,20))

# Example 3: Constructor with one parameter

class myclass3():
    name = "AK"
    def __init__(self,name):
        print(name)
        print(self.name)
mc11 = myclass3("Kiran")

# Example 9: # important
# Req: create emp class
# which will accept three parameters
# print data all the parameters

class emp():

    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
    def display(self):
        print(self.id,self.name,self.sal)
    # def __str__(self): # return only string value
    #     return (self.name)

e1 = emp(101,"AK", 1020202)
e1.display()
# print(e1) # return only string value

e2 = emp(102,"rat", 902002)
e2.display()