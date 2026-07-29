#Example 1:

# class myclass1:
#     def myfunc1(self):
#         pass
#     def display(self):
#         print("Ak")
#
# details1 = myclass1() #this object
# details1.display()


#Example 2: Passing argument

class Employee:

    def empname(self, name):
        print("Employee name:", name)

    def empid(self, emp_id):
        print("ID of employee:", emp_id)


emp = Employee()

emp.empname("AK THE MASS")
emp.empid(1234)