class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

rect1 = Rectangle(12, 6)
print("Area of rectangle:", rect1.area())

rect2 = Rectangle(8, 4)
print("Perimeter of rectangle:", rect2.perimeter())