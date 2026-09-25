## Question: Build a Student Management System using Python OOP.

class Student:

    # Class variable
    total_students = 0

    # Constructor
    def __init__(self, name, email, student_id, course, marks):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.course = course
        self.marks = marks

        # Increase total student count
        Student.total_students += 1

    # Instance method
    def display_details(self):
        """Display student details."""

        print("Name:", self.name)
        print("Email:", self.email)
        print("Student ID:", self.student_id)
        print("Course:", self.course)
        print("Marks:", self.marks)

    # Instance method
    def update_marks(self, new_marks):
        """Update the student's marks."""

        self.marks = new_marks

    # Instance method
    def calculate_average(self):
        """Calculate the average marks."""

        total = 0

        for mark in self.marks:
            total += mark

        average = round(total / len(self.marks), 2)

        return average

    # Class method
    @classmethod
    def get_total_students(cls):
        """Return the total number of students."""

        return cls.total_students


# Create student objects

student1 = Student(
    "Aman",
    "aman@gmail.com",
    101,
    "Data Science",
    [80, 85, 90]
)

student2 = Student(
    "Ravi",
    "ravi@gmail.com",
    102,
    "Python",
    [70, 75, 80]
)

student3 = Student(
    "Priya",
    "priya@gmail.com",
    103,
    "AI",
    [90, 95, 88]
)


# Display student details

print("===== Student 1 =====")
student1.display_details()

print("\n===== Student 2 =====")
student2.display_details()

print("\n===== Student 3 =====")
student3.display_details()


# Calculate average marks

print("\n===== Average Marks =====")

print("Aman Average:", student1.calculate_average())
print("Ravi Average:", student2.calculate_average())
print("Priya Average:", student3.calculate_average())


# Update marks

print("\n===== Updating Aman Marks =====")

student1.update_marks([90, 92, 95])

print("Updated Marks:", student1.marks)
print("New Average:", student1.calculate_average())


# Display total number of students

print("\n===== Total Students =====")

print("Total Students:", Student.get_total_students())