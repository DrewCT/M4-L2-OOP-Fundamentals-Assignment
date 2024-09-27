class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The new owner of vehicle '{self.registration_number}' has been updated to {self.owner}")

car = Vehicle("Y12345", "Car", "LeBron James")
bike = Vehicle("Z09876", "Motorcycle", "Jane Doe")

print(f"Vehicle: {car.registration_number}, Type: {car.type}, Owner: {car.owner}")
print(f"Vehicle: {bike.registration_number}, Type: {bike.type}, Owner: {bike.owner}\n")

car.update_owner("Chris Brown")
bike.update_owner("Don Toliver")

print(f"\nUpdated Vehicle: {car.registration_number}, Type: {car.type}, Owner: {car.owner}")
print(f"Updated Vehicle: {bike.registration_number}, Type: {bike.type}, Owner: {bike.owner}\n")