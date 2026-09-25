## Build a mini vehicle rental application.

class Vehicle:
    """Represent a general vehicle."""

    def __init__(self, vehicle_number, brand, model, rental_price_per_day):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day

    def calculate_rent(self, days):
        """Calculate total rental cost."""

        total_rent = self.rental_price_per_day * days

        print("Rental Days:", days)
        print("Total Rent:", total_rent)

        return total_rent

    @staticmethod
    def is_valid_duration(days):
        """Validate rental duration."""

        return days > 0


class Car(Vehicle):
    """Represent a car."""

    def __init__(
        self,
        vehicle_number,
        brand,
        model,
        rental_price_per_day,
        number_of_seats
    ):
        super().__init__(
            vehicle_number,
            brand,
            model,
            rental_price_per_day
        )

        self.number_of_seats = number_of_seats

    def display_car_details(self):
        """Display car details."""

        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Rental Price Per Day:", self.rental_price_per_day)
        print("Number of Seats:", self.number_of_seats)


class Bike(Vehicle):
    """Represent a bike."""

    def __init__(
        self,
        vehicle_number,
        brand,
        model,
        rental_price_per_day,
        engine_capacity
    ):
        super().__init__(
            vehicle_number,
            brand,
            model,
            rental_price_per_day
        )

        self.engine_capacity = engine_capacity

    def display_bike_details(self):
        """Display bike details."""

        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Rental Price Per Day:", self.rental_price_per_day)
        print("Engine Capacity:", self.engine_capacity)


# Create 2 Car objects

car1 = Car(
    "KA01AB1234",
    "Toyota",
    "Innova",
    2500,
    7
)

car2 = Car(
    "KA02CD5678",
    "Hyundai",
    "Creta",
    2000,
    5
)


# Create 2 Bike objects

bike1 = Bike(
    "KA03EF9012",
    "Royal Enfield",
    "Classic 350",
    800,
    "349cc"
)

bike2 = Bike(
    "KA04GH3456",
    "Honda",
    "Activa 6G",
    500,
    "109cc"
)


# Display car details

print("===== Car 1 =====")
car1.display_car_details()

print("\n===== Car 2 =====")
car2.display_car_details()


# Display bike details

print("\n===== Bike 1 =====")
bike1.display_bike_details()

print("\n===== Bike 2 =====")
bike2.display_bike_details()


# Demonstrate rental calculation

print("\n===== Car Rental =====")

if Vehicle.is_valid_duration(3):
    car1.calculate_rent(3)
else:
    print("Invalid rental duration.")


print("\n===== Bike Rental =====")

if Vehicle.is_valid_duration(5):
    bike1.calculate_rent(5)
else:
    print("Invalid rental duration.")


# Demonstrate invalid duration

print("\n===== Duration Validation =====")

print("Duration 5:", Vehicle.is_valid_duration(5))
print("Duration 0:", Vehicle.is_valid_duration(0))
print("Duration -2:", Vehicle.is_valid_duration(-2))


# Demonstrate inherited method

print("\n===== Inherited Method =====")

car2.calculate_rent(2)
bike2.calculate_rent(4)