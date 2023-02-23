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

    def _init_(self, drawing_api):
        self.drawing_api = drawing_api

    def draw(self):
        pass

class Circle(Shape):
    
    def _init_(self, x, y, radius, drawing_api):
        super()._init_(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

class Square(Shape):
    def _init_(self, x, y, side, drawing_api):
        super()._init_(drawing_api)
        self.x = x
        self.y = y
        self.side = side

class DrawingAPI1:
    def draw_circle(self, x, y, radius):
        print(f"API1 desenhando um círculo em ({x}, {y}) com raio {radius}")

    def draw_square(self, x, y, side):
        print(f"API1 desenhando um quadrado em ({x}, {y}) com lado {side}")

class DrawingAPI2:
    def draw_circle(self, x, y, radius):
        print(f"API2 desenhando um círculo em ({x}, {y}) com raio {radius}")

    def draw_square(self, x, y, side):
        print(f"API2 desenhando um quadrado em ({x}, {y}) com lado {side}")


# Exemplo de uso
if __name__ == "__main__":
    # Criando um círculo com a API1
    circle1 = Circle(1, 2, 3, DrawingAPI1())
    circle1.draw()

    # Criando um quadrado com a API2
    square1 = Square(4, 5, 6, DrawingAPI2())
    square1.draw()