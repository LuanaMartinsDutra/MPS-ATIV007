""""
O padrão de projeto Bridge é usado quando é necessário separar uma abstração
da sua implementação de forma que ambas possam ser modificadas independentemente
uma da outra. Ele permite que uma abstração possa variar independentemente das suas
implementações, o que é muito útil em situações em que as implementações devem ser alteradas
ou substituídas sem afetar a abstração.
"""

""""
    Classe abstrata que define uma forma geométrica.
"""
class Shape:
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)


class Square(Shape):
    def __init__(self, x, y, size, drawing_api):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        self.drawing_api.draw_square(self.x, self.y, self.size)


class DrawingAPIOne:
    def draw_circle(self, x, y, radius):
        print(f"API 1 desenha um círculo de raio {radius} na posição ({x}, {y})")

    def draw_square(self, x, y, size):
        print(f"API 1 desenha um quadrado de lado {size} na posição ({x}, {y})")


class DrawingAPITwo:
    def draw_circle(self, x, y, radius):
        print(f"///////////////////////////////////////////////////////////////")
        print(f"API 2 desenha um círculo de raio {radius} na posição ({x}, {y})")
        print(f"///////////////////////////////////////////////////////////////\n")

    def draw_square(self, x, y, size):
        print(f"///////////////////////////////////////////////////////////////")
        print(f"API 2 desenha um quadrado de lado {size} na posição ({x}, {y})")
        print(f"///////////////////////////////////////////////////////////////\n")


def main():
    circle1 = Circle(1, 2, 3, DrawingAPIOne())
    circle1.draw()

    square1 = Square(5, 7, 9, DrawingAPITwo())
    square1.draw()


if __name__ == "__main__":
    main()