shapes = [
    {"type": "Square", "area": 150.5},
    {"type": "Rectangle", "area": 80},
    {"type": "Rectangle", "area": 660},
    {"type": "Circle", "area": 68.2},
    {"type": "Triangle", "area": 20}
]


class Shape:
    def __init__(self, type, area):
        self.type = type
        self.area = area

    def __str__(self):
        return f"{self.type} with area size {self.area}"


class Triangle(Shape):
    def __init__(self, area):
        super().__init__("Triangle", area)


class Circle(Shape):
    def __init__(self, area):
        super().__init__("Circle", area)


class Square(Shape):
    def __init__(self, area):
        super().__init__("Square", area)


class Rectangle(Shape):
    def __init__(self, area):
        super().__init__("Rectangle", area)

    # ...


name_to_shape = {"Rectangle": Rectangle, "Triangle": Triangle,
                 "Circle": Circle, "Square": Square}

for i, data in enumerate(shapes):
    shape_class = name_to_shape[data["type"]]
    shape = shape_class(data["area"])
    print(f"{i + 1} - {shape}")
