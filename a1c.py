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

    # def print(self):
    #     print(f"{self.type} with area size {self.area}")


i = 1
for data in shapes:
    shape = Shape(data["type"], data["area"])
    print(f"{i} - {shape}")
    i += 1
