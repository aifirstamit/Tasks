## Question: Create a base class called Employee and a child class Developer using inheritance.

class Employee:
    """Represent a general employee."""

    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        """Display employee details."""

        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


class Developer(Employee):
    """Represent a developer who inherits from Employee."""

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        programming_language,
        experience
    ):
        # Call the parent class constructor
        super().__init__(
            employee_id,
            name,
            salary,
            department
        )

        # Developer-specific attributes
        self.programming_language = programming_language
        self.experience = experience

    def display_developer_details(self):
        """Display developer-specific details."""

        self.display_details()

        print("Programming Language:", self.programming_language)
        print("Experience:", self.experience, "years")


# Create Employee objects

employee1 = Employee(
    101,
    "Aman",
    45000,
    "HR"
)

employee2 = Employee(
    102,
    "Ravi",
    50000,
    "Finance"
)


# Create Developer object

developer1 = Developer(
    103,
    "Priya",
    75000,
    "Technology",
    "Python",
    3
)


# Display Employee details

print("===== Employee 1 =====")
employee1.display_details()

print("\n===== Employee 2 =====")
employee2.display_details()


# Display Developer details

print("\n===== Developer =====")
developer1.display_developer_details()


# Demonstrate inherited functionality

print("\n===== Inherited Method =====")

developer1.display_details()