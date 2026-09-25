## Build a mini Super30 Learning Platform.

class User:
    """Represent a general user of the Super30 platform."""

    # Class variable
    total_users = 0

    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

        # Increase total user count
        User.total_users += 1

    def display_user_info(self):
        """Display common user information."""

        print("Name:", self.name)
        print("Email:", self.email)
        print("User ID:", self.user_id)

    @classmethod
    def get_total_users(cls):
        """Return the total number of users."""

        return cls.total_users

    @staticmethod
    def is_valid_email(email):
        """Check whether an email contains @."""

        return "@" in email


class Student(User):
    """Represent a student on the Super30 platform."""

    def __init__(
        self,
        name,
        email,
        user_id,
        course_name
    ):
        # Call parent class constructor
        super().__init__(
            name,
            email,
            user_id
        )

        self.course_name = course_name
        self.completed_assignments = []

    def register_course(self, course_name):
        """Register the student for a course."""

        self.course_name = course_name

        print(
            self.name,
            "registered for",
            self.course_name
        )

    def submit_assignment(self, assignment_name):
        """Submit an assignment."""

        self.completed_assignments.append(assignment_name)

        print(
            self.name,
            "submitted:",
            assignment_name
        )

    def display_student_info(self):
        """Display student information."""

        self.display_user_info()

        print("Course:", self.course_name)

        print(
            "Completed Assignments:",
            self.completed_assignments
        )


class Mentor(User):
    """Represent a mentor on the Super30 platform."""

    def __init__(
        self,
        name,
        email,
        user_id,
        expertise,
        students_assigned
    ):
        # Call parent class constructor
        super().__init__(
            name,
            email,
            user_id
        )

        self.expertise = expertise
        self.students_assigned = students_assigned

    def assign_student(self):
        """Increase the number of assigned students."""

        self.students_assigned += 1

        print(
            "Student assigned to",
            self.name
        )

    def display_mentor_info(self):
        """Display mentor information."""

        self.display_user_info()

        print("Expertise:", self.expertise)

        print(
            "Students Assigned:",
            self.students_assigned
        )


# Create Student objects

student1 = Student(
    "Aman",
    "aman@example.com",
    101,
    "Python"
)

student2 = Student(
    "Ravi",
    "ravi@example.com",
    102,
    "Data Science"
)


# Create Mentor objects

mentor1 = Mentor(
    "Priya",
    "priya@example.com",
    201,
    "Python and AI",
    2
)

mentor2 = Mentor(
    "Rahul",
    "rahul@example.com",
    202,
    "Data Science",
    3
)


# Display student information

print("===== Student 1 =====")
student1.display_student_info()

print("\n===== Student 2 =====")
student2.display_student_info()


# Display mentor information

print("\n===== Mentor 1 =====")
mentor1.display_mentor_info()

print("\n===== Mentor 2 =====")
mentor2.display_mentor_info()


# Register student for a course

print("\n===== Course Registration =====")

student1.register_course("Advanced Python")


# Submit assignments

print("\n===== Assignment Submission =====")

student1.submit_assignment("Python Loop Task")
student1.submit_assignment("OOP Task")


student2.submit_assignment("Data Science Task")


# Assign students to mentors

print("\n===== Mentor Assignment =====")

mentor1.assign_student()
mentor2.assign_student()


# Validate email using static method

print("\n===== Email Validation =====")

print(
    "Aman email:",
    User.is_valid_email("aman@example.com")
)

print(
    "Invalid email:",
    User.is_valid_email("amanexample.com")
)


# Display updated student information

print("\n===== Updated Student 1 =====")

student1.display_student_info()


# Display updated mentor information

print("\n===== Updated Mentor 1 =====")

mentor1.display_mentor_info()


# Display total number of users

print("\n===== Total Users =====")

print(
    "Total Users Created:",
    User.get_total_users()
)