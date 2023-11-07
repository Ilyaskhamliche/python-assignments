#File-Name:M03_Lab_List_Functions_Classes.py
#Author: Ilyas Khamliche
#Date:11/7/2023
#Purpose: coding, designing, and utilizing classes in Python
# Defining a superclass called Vehicle a vehicle_type attribute
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
# Subclass called Automobile that inherits from the supercalss Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)
# Displays the the attributes the car
def main():
    print("Welcome to the Vehicle Information App")
    vehicle_type = "car"  # Set the vehicle type to "car"
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Create an Automobile object with user input
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    print("\nVehicle Information:")
    car.display_info()

if __name__ == "__main__":
    main()
