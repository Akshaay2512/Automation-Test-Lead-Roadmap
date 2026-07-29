#Example 1:
global_var = 20  #global varibale

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

# Example 3: global and local variable with same name

xy =100

def func3():
    global xy
    xy=200  #global variable 100 is replaced with local variable so 200
    print(xy)

func3()
print(xy)


