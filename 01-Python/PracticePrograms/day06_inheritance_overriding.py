# ## Objective of inheritance
# 1. Code re-usability
# 2. Avoid duplication

# ## Types of inheritance
# 1. Single - one parent and one child
# 2. Multi level - One parent and multiple child (each child class act as parent)
# 3. Hierarchy - One parent and multiple child (each child has different attributes)
# 4. Multiple - multiple parent one child

#Example 1: Single inheritance
print("==" * 20, "Single Inheritance", "==" * 20)

class A:
    def m1(self):
        print("This m1 method from class A")

class B(A): # calling class A(as parent)
    def m2(self):
        print("This is m2 method from class B")

objb=B()
objb.m1() # this from class A but inherited
objb.m2()

print("==" * 20, "Single Inheritance", "==" * 20)

#Example 2: Single inheritance

class A1():
    x,y = 10,20
    def m11(self):
        print(self.x+self.y)

class B1(A1):
    a,b = 100,200
    def m22(self):
        print(self.a+self.b)

obj1=B1()
obj1.m11()
obj1.m22()

print("==" * 20, "Multi level Inheritance", "==" * 20)

#Example 3: multi level inheritance

class A11():
    x,y = 10,20
    def m111(self):
        print(self.x+self.y)

class B11(A11):
    a,b = 200,100
    def m222(self):
        print(self.a-self.b)

class C11(B11):
    i,j = 20,10
    def m333(self):
        print(self.i*self.j)

objc = C11()
objc.m111()
objc.m222()
objc.m333()

print("==" * 20, "Hierarchy Inheritance", "==" * 20)

#Example 4: Hierarchy inheritance

class AK():
    x, y = 10, 20
    def m111(self):
        print(self.x + self.y)

class RAT(AK):
    a, b = 200, 100
    def m222(self):
        print(self.a - self.b)

class Gulu(AK):
    i, j = 20, 10
    def m333(self):
        print(self.i * self.j)

fam = RAT()
fam.m111()
fam.m222()

fam1 = Gulu()
fam1.m111()
fam1.m333()

print("==" * 20, "Multiple Inheritance", "==" * 20)

#Example 5: Multiple inheritance

class AK1():
    x, y = 10, 20
    def m111(self):
        print(self.x + self.y)

class RAT1():
    a, b = 200, 100
    def m222(self):
        print(self.a - self.b)

class Gulu1(AK1,RAT1):
    i, j = 20, 10
    def m333(self):
        print(self.i * self.j)

kid = Gulu1()
kid.m111()
kid.m222()
kid.m333()

print("==" * 20, "same method name(Overriding) ", "==" * 20)

#Example 6: overriding methods

class parent():
    def m1(self,a,b):
        return a+b

class child(parent):
    def m1(self):
        print("This is child")
        print(super().m1(2,2))  # to call parent method

res = child()
res.m1()

print("==" * 20, "same method name(Overriding) ", "==" * 20)

#Example 7:

class AA:
    a,b = 10,20

class BB(AA):
    i,j= 100,200
    def m1(self,x,y):
        print(x + y)    # local variables
        print(self.i + self.j) # class variables
        print(self.a + self.b) # class variables

objb = BB()
objb.m1(50,20)

print("==" * 20, "same variable name(Overriding) ", "==" * 20)

#Example 8: overriding variables

class parent1:
    name = "AK"

class child1(parent1):
    name = "Rat"
    def test(self):
        print(super().name)   # to print parent class name

cobj = child1()
print(cobj.name)
cobj.test()

print("==" * 20, "Overriding methods ", "==" * 20)

#Example 9: overriding methods

class bank():
    def rateofinterest(self):
        return 0

class Xbank(bank):
    def rateofinterest(self):
        return 10

class Ybank(bank):
    def rateofinterest(self):
        return 20

objx = Xbank()
print(objx.rateofinterest())

objy = Ybank()
print(objy.rateofinterest())

print("==" * 20, "Overloading ", "==" * 20)

#Example 10: Overloading(polymorphism) one method can have multiple form parameter can be passed or not

class Human():
    def sayhello(self,name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hellooo")

h = Human()
h.sayhello("Ak")
h.sayhello()

#Example 11: Overloading(polymorphism)

class calc():
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

calobj = calc()
calobj.add() # without using parameters
calobj.add(10,20) # without using all parameters
calobj.add(10,20,30) # with all parameters


