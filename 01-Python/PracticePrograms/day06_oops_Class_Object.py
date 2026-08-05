#Example 1:

class myclass1:
    def myfunc1(self):
        pass
    def display(self):
        print("Ak")

details1 = myclass1() #this object
details1.display()


#Example 2: Passing argument

class Employee:

    def empname(self, name):
        print("Employee name:", name)

    def empid(self, emp_id):
        print("ID of employee:", emp_id)


emp = Employee()

emp.empname("AK THE MASS")
emp.empid(1234)

#Example 3: instance method and static method

class myclass1:
    def m1(self):
        print("This is instance...")
    @staticmethod #common method >>> directly by using class we can call the method
    def m2(self,num):
        print(num)

mc=myclass1()
mc.m1()

myclass1.m2(10,20)


#Example 4: Class variables

class myclass():
    a,b = 10,20 #class variables
    def add(self):
        print(self.a+self.b)     ## Important -  whenever calling class variables using self.
    def mul(self):
        print(self.a * self.b)

mc = myclass()
mc.add()
mc.mul()

#Example 5: all  variables

i,j = 15,25    # global variable

class myclass2():
    a,b = 10,20         # class variable
    def add(self,x,y):    # local variables
        print(x+y)
        print(self.a + self.b)
        print(i+j)

mc = myclass2()
mc.add(10,20)

#Example 5: all  variables names same

a,b = 15,20    # global variable

class myclass2():
    a,b = 10,20         # class variable
    def add(self,a,b):    # local variables
        print(a+b)
        print(self.a + self.b)
        print(globals()['a'] + globals()['b'])
mc = myclass2()
mc.add(100,200)

#Example 6: one class multiple objects

class myclass3():
    def display(self,name):
        print("This is display method")
        print(name)

obj1 = myclass3()
obj1.display("AK")

oj2 = myclass3()
oj2.display("Kiran")
