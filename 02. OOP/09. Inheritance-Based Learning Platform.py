## Design a small learning platform using inheritance.

class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    def display_info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("User ID:", self.user_id)

    def display_role(self):
        print("Role: User")


class Student(User):
    def __init__(self, name, email, user_id, course):
        super().__init__(name, email, user_id)
        self.course = course

    def display_role(self):
        print("Role: Student")

    def submit_assignment(self, assignment):
        print(self.name, "submitted:", assignment)


class Mentor(User):
    def __init__(self, name, email, user_id, subject):
        super().__init__(name, email, user_id)
        self.subject = subject

    def display_role(self):
        print("Role: Mentor")

    def teach_course(self):
        print(self.name, "is teaching", self.subject)


class Admin(User):
    def __init__(self, name, email, user_id, department):
        super().__init__(name, email, user_id)
        self.department = department

    def display_role(self):
        print("Role: Admin")

    def manage_platform(self):
        print(self.name, "is managing the learning platform")


# Create objects
student = Student(
    "Aman",
    "aman@example.com",
    "S101",
    "Python"
)

mentor = Mentor(
    "Priya",
    "priya@example.com",
    "M101",
    "Data Science"
)

admin = Admin(
    "Rahul",
    "rahul@example.com",
    "A101",
    "Administration"
)


# Student
print("===== Student =====")
student.display_info()
student.display_role()
print("Course:", student.course)
student.submit_assignment("Python Assignment")


# Mentor
print("\n===== Mentor =====")
mentor.display_info()
mentor.display_role()
print("Subject:", mentor.subject)
mentor.teach_course()


# Admin
print("\n===== Admin =====")
admin.display_info()
admin.display_role()
print("Department:", admin.department)
admin.manage_platform()


# Method overriding
print("\n===== Method Overriding =====")

users = [student, mentor, admin]

for user in users:
    user.display_role()