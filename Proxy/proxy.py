class Faculdade:

	def estudando(self):
		print("Estudando...\n")


class FaculdadeProxy:
	''' Instancia o objeto Faculdade apenas se não tiver dívidas.
    Ao invés de criar o objeto quando a aplicação inicializa,
    ele atrasa a inicialização do objeto para um momento que ela seja realmente necessária.'''

	def __init__(self):

		self.divida = 1000
		self.Faculdade = None

	def estudando(self):

		print("Vendo o valor total de suas dívidas...")
		if self.divida <= 500:
			# Se as dívidas são menores que 500 reais, deixe ele estudar
			self.Faculdade = Faculdade()
			self.Faculdade.estudando()
		else:
			# Caso não, proíba dele estudar
			print("Você tem mais de 500 reais de dívida, pague suas dívidas primeiro.\n")


if __name__ == "__main__":
	
	# Instanciando o proxy
	FaculdadeProxy = FaculdadeProxy()

	''' Como o cliente possui uma dívida de 1000 reais,
    ele vai ser proibido de estudar na faculdade até
    pagar as dívidas '''
	FaculdadeProxy.estudando()

	# Mudança das dívidas para 100 reais
	FaculdadeProxy.divida = 100
	
	# Agora sim ele pode estudar
	FaculdadeProxy.estudando()
