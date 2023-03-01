# VIsitor

# ALexandre Bruno Mota dos Santos

# Importa a classe ABC (Abstract Base Class) e o decorador abstractmethod
from abc import ABC, abstractmethod


# Define uma classe abstrata Shape que herda da classe abstrata ABC


class Shape(ABC):
    # Define um método abstrato move com dois parâmetros
    @abstractmethod
    def move(self, x, y):
        pass
    
    # Define um método abstrato draw
    @abstractmethod
    def draw(self):
        pass
    
    # Define um método abstrato accept com um parâmetro v
    @abstractmethod
    def accept(self, v):
        pass


# A classe Circle representa um círculo e herda da classe Shape.


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def draw(self):
        print(f"Drawing circle with center ({self.x}, {self.y}) and radius {self.radius}")
        
    def accept(self, v):
        v.visit_circle(self)


# A classe Rectangle representa um retângulo e herda da classe Shape.


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def draw(self):
        print(f"Drawing rectangle with top left corner ({self.x}, {self.y}) and dimensions ({self.width}, {self.height})")
        
    def accept(self, v):
        v.visit_rectangle(self)


# A classe CompoundShape representa uma forma composta que consiste em outras formas.


class CompoundShape(Shape):
    def __init__(self):
        self.shapes = []
        
    def add(self, shape):
        self.shapes.append(shape)
        
    def move(self, x, y):
        for shape in self.shapes:
            shape.move(x, y)
        
    def draw(self):
        for shape in self.shapes:
            shape.draw()
        
    def accept(self, v):
        v.visit_compound_shape(self)


# A classe Visitor representa um visitante que visita cada forma e executa uma operação nela.
class Visitor:
    def visit_dot(self, dot):
        pass
    
    def visit_circle(self, circle):
        pass
    
    def visit_rectangle(self, rectangle):
        pass
    
    def visit_compound_shape(self, compound_shape):
        pass
    

# A classe XMLExportVisitor representa um visitante que exporta cada forma para XML.


class XMLExportVisitor(Visitor):
    def visit_dot(self, dot):
        print("Exporting dot to XML")
    
    def visit_circle(self, circle):
        print("Exporting circle to XML")
    
    def visit_rectangle(self, rectangle):
        print("Exporting rectangle to XML")
    
    def visit_compound_shape(self, compound_shape):
        print("Exporting compound shape to XML")
        

# A classe Application representa a aplicação que contém uma lista de todas as formas e permite exportá-las.


class Application:
    def __init__(self):
        self.allShapes = []  # Inicializa a lista de formas vazia.
    
    def add_shape(self, shape):
        self.allShapes.append(shape)
    
    def export(self):
        exportVisitor =
