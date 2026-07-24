class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("\n----- Rectangle -----")
        print("Length :", self.length)
        print("Width :", self.width)
        print("Area :", self.area())
        print("Perimeter :", self.perimeter())


length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

rect = Rectangle(length, width)

rect.display()