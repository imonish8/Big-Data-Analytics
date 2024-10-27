class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return f"Area if the circle : {self.pi*self.radius**2}"

class Rectangle:
    def __init__(self, long, wide):
        self.long = long
        self.wide = wide

    def calculate_area(self):
        return f"area of rectanfle  {self.long*self.wide}"

class prism:
    def __init__(self, long, wide, height):
        self.long = long
        self.wide = wide
        self.height = height
    def calculate_area(self):
        return f"area of cuboid : {2*(self.long*self.wide+self.wide*self.height+self.height*self.long)}"

Shapes = [Rectangle(5,10), Circle(5), prism(7,8,9)]

for shape in Shapes:
    print("area ", shape.calculate_area())


