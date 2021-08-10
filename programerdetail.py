class programmer:
    
    def display_details(self):
        for i in range(3):
            print(f"\n Name of {i} Employee is :{self.Employee_name}")
            print(f"\n Salary of {i} Employee is :{self.Employee_salary}")
            print(f"\n Compamy of {i} Employee is :{self.Employee_company}")
            print(f"\n Age of {i} Employee is :{self.Employee_age}")

obj=programmer()
obj.Employee_name="mona Gupta"
obj.Employee_salary=1000
obj.Employee_Company="google"
obj.Employee_age= 20
obj.display_details()
          