## Create an Employee Management System in Python.

class Employee:
    def __init__(self, employee_id, name, department, salary, designation):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.designation = designation

    def display_employee_info(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Designation:", self.designation)

    def update_salary(self, new_salary):
        self.salary = new_salary
        print("Salary updated successfully.")
        print("New Salary:", self.salary)

    def calculate_annual_salary(self):
        annual_salary = self.salary * 12
        print("Annual Salary:", annual_salary)
        return annual_salary


# Create 5 employee objects

employee1 = Employee(
    "E101", "Amit", "IT", 60000, "Software Engineer"
)

employee2 = Employee(
    "E102", "Priya", "HR", 50000, "HR Executive"
)

employee3 = Employee(
    "E103", "Rahul", "Finance", 55000, "Accountant"
)

employee4 = Employee(
    "E104", "Neha", "Marketing", 48000, "Marketing Executive"
)

employee5 = Employee(
    "E105", "Arjun", "Operations", 52000, "Operations Manager"
)


# Display employee information

print("===== Employee 1 =====")
employee1.display_employee_info()

print("\n===== Employee 2 =====")
employee2.display_employee_info()

print("\n===== Employee 3 =====")
employee3.display_employee_info()

print("\n===== Employee 4 =====")
employee4.display_employee_info()

print("\n===== Employee 5 =====")
employee5.display_employee_info()


# Update salary

print("\n===== Salary Update =====")
employee1.update_salary(65000)


# Calculate annual salary

print("\n===== Annual Salary =====")
employee1.calculate_annual_salary()
employee2.calculate_annual_salary()
employee3.calculate_annual_salary()
employee4.calculate_annual_salary()
employee5.calculate_annual_salary()