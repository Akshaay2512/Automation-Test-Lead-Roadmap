# Employee experience for one person


print("=" * 50)
print("Employee Details")
print("=" * 50)

# Employee Details
Emp_ID = 12345
Emp_Name = "Akshaay"
Emp_Salary = 120000
Emp_exp = 6

print(f"Employee ID  : {Emp_ID}")
print(f"Employee Name  : {Emp_Name}")
print(f"Employee Salary  : {Emp_Salary}")
print(f"Employee experience  : {Emp_exp}")


#Role based on experience
if Emp_exp >= 8:
    print("He is eligible for senior")
else:
    print("Not Eligible")

# Employee experience for multiple person