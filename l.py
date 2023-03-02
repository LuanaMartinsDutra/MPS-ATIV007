class Forma:
	def area(self):
		pass
		
		
class Retangulo(Forma):
	def __init__(self, altura, largura):
	self.altura = altura
	self.largura = largura
	
	def area(self):
		return self.altura*self.largura
	
class Triangulo(Forma):
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura
	def area(self):
		return self.altura*self.largura / 2
