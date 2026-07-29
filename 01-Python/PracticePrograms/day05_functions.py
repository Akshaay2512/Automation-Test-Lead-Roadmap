# Methods of functions:

# 1. function does not take arguments not return any value(none)
# 2. function does not take arguments but return some values
# 3. function takes arguments but no return value
# 4. function takes arguments and also return value

#1. Function does not take arguments and does not return any value

def launch_browser():
    print("Chrome Browser Launched")

launch_browser()

#2. Function does not take arguments but returns a value

def get_application_url():
    return "https://www.saucedemo.com"

url = get_application_url()

print(url)

#3. Function takes arguments but does not return any value

def login(username, password):
    print("Username:", username)
    print("Password:", password)

login("standard_user", "secret_sauce")

#4. Function takes arguments and also returns a value

def validate_login(username, password):

    if username == "admin" and password == "admin123":
        return "Login Successful"
    else:
        return "Invalid Credentials"

result = validate_login("admin", "admin123")

print(result)

#Example 1 creation/declare function

def myfunc1():
    print("helllo")

myfunc1() # calling function

#Example 2: function with single parameter

def myfunc2(name):
    print("hello", name)

myfunc2("Akshaay")

#Example 3: function with multiple parameter with return:

def myfunc3(a,b):
    return (a+b)

sum = myfunc3(100, 200) # method 1
print(sum)

print(myfunc3(10,20)) # method 2

#Example 4: function without parameter but with return:

def myfunc4():
    return

print(myfunc4()) #none

#Example 5: function with multiple parameter without return

def myfunc5(a, b):
    print(a+b)    # without return

myfunc5(105,205)

def myfunc6(a, b):
    return (a+b)

print(myfunc6(10,20))


