#Printing 10 orders
order = 1

while order <= 10:
    print(f"Processing Order {order}")
    order = order + 1

print("All Orders Processed Successfully")

#You have 5 login attempts.

attempt =1

while attempt<=5:
    print(f"You on attempt {attempt}")
    attempt = attempt+1
print("Maximum attempts reached")

#Imagine Selenium has 3 browsers to execute tests

browser = 1

while browser<=3:
    print(f"Executing Test in Browser {browser}")
    browser = browser+1
print("Execution done!!!")

# Orders with failure

orders = 1

while orders <= 10:
    if orders == 3:
        print(f"Order {orders} - Failed ❌")
    elif orders == 7:
        print(f"Order {orders} - Failed ❌")
    else:
        print(f"Order {orders} - Processed Successfully ✅")
    orders = orders+1



