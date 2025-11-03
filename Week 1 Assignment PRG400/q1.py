class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Vehicle Brand:", self.brand)
        print("Vehicle Model:", self.model)


brand = input("Enter vehicle brand: ")
model = input("Enter vehicle model: ")


v1 = Vehicle(brand, model)
v1.display_info()
