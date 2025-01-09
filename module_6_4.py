class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides) if len(sides) == self.sides_count else [1] * self.sides_count
        self.__color = list(color) if Figure.__is_valid_color(*color) else [0, 0, 0]
        self.filled = False

    @staticmethod
    def __is_valid_color(r,g,b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_sides(*sides):
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.14159265359)

    def get_square(self):
        return 3.14159265359 * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0] / (2 * 3.14159265359)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side = sides[0] if len(sides) == 1 and isinstance(sides[0], int) and sides[0] > 0 else 1
        super().__init__(color, *(side for _ in range(self.sides_count)))

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], int) and new_sides[0] > 0:
            self.__sides = [new_sides[0]] * self.sides_count

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3



circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
