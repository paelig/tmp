class Point:
    def __init__(self, builder):
        self.x = builder.x
        self.y = builder.y
        self.color = builder.color
        self.stroke = builder.stroke
        self.shadow = builder.shadow

    def __str__(self):
        return f'Point: x={self.x}, y={self.y}, color={self.color}, stroke={self.stroke}, shadow={self.shadow}'


class PointBuilder:
    def __init__(self, x=0, y=0, color='blue'):
        self.x = x
        self.y = y
        self.color = color
        self.stroke = False
        self.shadow = False

    def add_stroke(self):
        self.stroke = True
        return self

    def add_shadow(self):
        self.shadow = True
        return self

    def build(self):
        return Point(self)


# Использование
point = PointBuilder().build()
print(point)
point_with_shadow = PointBuilder(1, 3, "red").add_shadow().build()
print(point_with_shadow)
point_with_stroke = PointBuilder(-2, 9, "black").add_stroke().build()
print(point_with_stroke)
max_point = PointBuilder().add_stroke().add_shadow().build()
print(max_point)
