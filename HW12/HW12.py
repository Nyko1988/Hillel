# Доопрацюйте класс Pоint з заняття наступним чином: додайте перевірку координат x та y на числа за допомогою property
print('Ex. #1')

class Point:
    x = None
    y = None

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    @property
    def check_coord_digits(self):
        if type(self.y) == type(self.x) == int:
            return True
        else:
            return False


point3 = Point(0, 'a')
point4 = Point(0, 1)
print(f'are "{point3.x}" and "{point3.y}" are digits? : {point3.check_coord_digits}')
print(f'are "{point4.x}" and "{point4.y}" are digits? : {point4.check_coord_digits}')

# Доопрацюйте класс Line з заняття наступним чином: додайте можливість порівнювати лінії по довжині (==, !=, >=, <=, >, <) за допомогою відповідних методів
print('Ex. #2')
class Line:
    begin = None
    end = None

    def __init__(self, start, finish):
        self.begin = start
        self.end = finish

    def length_getter(self):
         k1 = self.begin.x - self.end.x
         k2 = self.begin.y - self.end.y

         res = (k1 ** 2 + k2 ** 2) ** 0.5
         return res

    def __eq__(self, other):  # ==
        equal = self.length_getter() == other.length_getter()
        return equal

    def __ne__(self, other):  # !=
        not_equal = self.length_getter() != other.length_getter()
        return not_equal

    def __lt__(self, other):  # <
        less = self.length_getter() < other.length_getter()
        return less

    def __le__(self, other):  # <=
        less_or_eque = self.length_getter() <= other.length_getter()
        return less_or_eque

    def __gt__(self, other):  # >
        more = self.length_getter() > other.length_getter()
        return more

    def __ge__(self, other):  # >=
        more_or_eque = self.length_getter() >= other.length_getter()
        return more_or_eque


point1 = Point(1, 6)
point2 = Point(2, 8)
point5 = Point(5, 20)
point6 = Point(1, 20)
line1 = Line(point1, point2)
line2 = Line(point5, point6)
print(f"lenght of 'line1' = {line1.length_getter()}")
print(f"lenght of 'line2' = {line2.length_getter()}")

print(f"{line1.length_getter()} == {line2.length_getter()} ->", line1 == line2)
print(f"{line1.length_getter()} != {line2.length_getter()} ->", line1 != line2)
print(f"{line1.length_getter()} > {line2.length_getter()} ->", line1 > line2)
print(f"{line1.length_getter()} < {line2.length_getter()} ->", line1 < line2)
print(f"{line1.length_getter()} <= {line2.length_getter()} ->", line1 <= line2)
print(f"{line1.length_getter()} >= {line2.length_getter()} ->", line1 >= line2)
