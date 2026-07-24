class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("\n----- Employee Details -----")
        print("Employee ID :", self.emp_id)
        print("Name :", self.name)
        print("Salary :", self.salary)

    def annual_salary(self):
        print("Annual Salary :", self.salary * 12)


emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
salary = float(input("Enter Monthly Salary: "))

emp = Employee(emp_id, name, salary)

emp.display()
emp.annual_salary()