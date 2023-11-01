class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __iadd__(self, other):
        self.radius += other
        return self

    def __isub__(self, other):
        self.radius -= other
        return self

    def __str__(self):
        return self.radius


circle1 = Circle(4)
circle2 = Circle(8)
print(circle1 == circle2)
print(circle1 > circle2)
print(circle1 < circle2)
print(circle1 <= circle2)
print(circle1 >= circle2)
circle1 += 2
print(circle1.radius)
