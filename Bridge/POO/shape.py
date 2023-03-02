from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def draw(self):
        pass