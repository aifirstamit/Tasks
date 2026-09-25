## Build a simple online learning platform using inheritance.

class Course:
    """Represent a general online course."""

    # Class variable
    course_count = 0

    def __init__(self, course_name, instructor, duration, price):
        self.course_name = course_name
        self.instructor = instructor
        self.duration = duration
        self.price = price

        # Increase course count whenever a course is created
        Course.course_count += 1

    def show_course_details(self):
        """Display course details."""

        print("Course Name:", self.course_name)
        print("Instructor:", self.instructor)
        print("Duration:", self.duration)
        print("Price:", self.price)

    def calculate_discount(self, discount_percentage):
        """Calculate discounted course price."""

        discount = self.price * discount_percentage / 100
        final_price = self.price - discount

        print("Discount:", discount)
        print("Final Price:", final_price)

        return final_price

    @classmethod
    def get_course_count(cls):
        """Return the total number of courses created."""

        return cls.course_count


class PremiumCourse(Course):
    """Represent a premium course."""

    def __init__(
        self,
        course_name,
        instructor,
        duration,
        price,
        mentor_support,
        live_sessions
    ):
        # Call parent class constructor
        super().__init__(
            course_name,
            instructor,
            duration,
            price
        )

        self.mentor_support = mentor_support
        self.live_sessions = live_sessions

    def show_premium_details(self):
        """Display premium course details."""

        self.show_course_details()

        print("Mentor Support:", self.mentor_support)
        print("Live Sessions:", self.live_sessions)


# Create normal Course objects

course1 = Course(
    "Python Basics",
    "Rahul Sharma",
    "6 Weeks",
    3000
)

course2 = Course(
    "Data Science",
    "Neha Singh",
    "8 Weeks",
    5000
)

course3 = Course(
    "Web Development",
    "Amit Kumar",
    "10 Weeks",
    6000
)


# Create PremiumCourse objects

premium_course1 = PremiumCourse(
    "Machine Learning",
    "Priya Verma",
    "12 Weeks",
    10000,
    "Yes",
    "Yes"
)

premium_course2 = PremiumCourse(
    "Generative AI",
    "Rohit Mehta",
    "10 Weeks",
    12000,
    "Yes",
    "Yes"
)


# Display normal course details

print("===== Course 1 =====")
course1.show_course_details()

print("\n===== Course 2 =====")
course2.show_course_details()

print("\n===== Course 3 =====")
course3.show_course_details()


# Display premium course details

print("\n===== Premium Course 1 =====")
premium_course1.show_premium_details()

print("\n===== Premium Course 2 =====")
premium_course2.show_premium_details()


# Demonstrate discount

print("\n===== Discount =====")
course1.calculate_discount(10)

premium_course1.calculate_discount(20)


# Demonstrate inherited functionality

print("\n===== Inherited Method =====")
premium_course1.show_course_details()


# Display total course count

print("\n===== Course Count =====")
print("Total Courses Created:", Course.get_course_count())