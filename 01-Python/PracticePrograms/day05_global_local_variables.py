#Example 1:
global_var = 20  #global variable

def func1():
    local_var=10  # local variable
    print(local_var)
    print(global_var)

func1()

#print(local_var)  #invalid can not call local variable outside function
print(global_var) # valid can be called anywhere inside and outside function

# Example 2: global and local variable with same name

xy =100

def func2():
    xy=200
    print(xy)

func2() #if variable names are same when calling it will first call only the variable inside the function
print("==" * 20)

# Example 3: global and local variable with same name so change the global variable value

xy =100

def func3():
    global xy
    xy=200  #global variable 100 is replaced with local variable so 200
    print(xy)

func3()
print(xy)

# Example 4:

x = 100

def func4():
    global x
    x = 500
    print(x)

func4() #500 without calling this func only x=100 will be displayed
print(x) #500 even when printed outside function

# Example 5: creation of global variable inside the function

def func5():
    global xz
    xz = 100
    print(x)

func5()
print(xz) # since it is local variable we can access even if it is inside function




