from abc import ABC, abstractmethod
class Pagamento (ABC):
	@abstractmethod
	def pagar(self):
		pass
		
class CartaoCredito(Pagmento):
	def pagar(self):
	# codigo pra pagar com cartao
	
class Boleto(Pagamento):
	def pagar(self):
	# codigo pra pagar com boleto
	
