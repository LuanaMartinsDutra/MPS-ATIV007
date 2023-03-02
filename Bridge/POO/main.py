from color import Color
from circle import Circle
from square import Square

# criando objetos Shape e Color
red_color = Color("vermelho")
green_color = Color("verde")
blue_color = Color("azul")
circle = Circle(red_color)
square = Square(green_color)

# desenhando formas em diferentes cores
circle.draw()
square.draw()