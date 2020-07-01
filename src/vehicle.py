class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()


car1.name = "Toyota"
car1.color = "Black"
car1.kind = "Car"
car1.value = 2090909
print(car1.description())
