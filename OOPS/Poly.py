class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):

        print("Move!")


class car(vehicle):
    pass


class boat(vehicle):
    def move(self):
        print("Sail!")


class plane(vehicle):
    def move(self):
        print("Fly!")


car1 = car("Ford", "Mustang")  # Create a Car object
boat1 = boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    if x is car1:
        print("First One:\n")

    print(x.brand)
    print(x.model)
    x.move()
    print("\n")
    if x is not plane1:   # missing parentheses fixed
        print("Next One:\n")
