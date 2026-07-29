# Positional arguments Definition: Values are assigned based on their position.
def student(name, age):
    print(name)
    print(age)

student("Akshaay", 30)

print("=" * 20)

#Keyword arguments Definition: Values are assigned using the parameter names, so order doesn't matter.
def student(name, age):
    print(name)
    print(age)

student(age=30, name="Akshaay")


# Example 1 :  Positional arguments

def argu1(i,j):
    print(i,j)

argu1(10,20)

print("=" * 20)

# Example 2 :  Keyword arguments(default values assigned

def argu2(i,j):
    print(i,j)

argu1(j=20,i=10) # mentioning like, this value needs to be applied for this arguments

print("=" * 20)

# Example 3 :  Keyword arguments

def argu3(i,j=10):
    print(i,j)

argu3(100) # positional arg
argu3(100,200) # positional arg

print("=" * 20)

print("=" * 20)

# Example 4 :  Keyword arguments

def greetings(name, greetmsg):
    print(greetmsg+"   "+name)

greetings(name="Ak", greetmsg="Good Morning") #Good Morning   Ak
greetings(greetmsg="Good Morning", name="Ak") #Good Morning   Ak

# Example 5 :  mix positional and keyword

def mydata(a,b,c):
    print(a,b,c)

mydata(10,20,30)  #Positional arguments
mydata(a=10,b=20,c=30)  #Keyword arguments
mydata(b=20,c=30,a=10)  #Keyword arguments does not need order

mydata(10,b=20,c=30) #Combination
mydata(10,20,c=30)
# mydata(10,20,b=30)

# Example 6 :

def largets(a,b):
    if a > b:
        return a,b
    else:
        return b,a

Result = largets(100,200)
print(Result)
print(type(Result))
