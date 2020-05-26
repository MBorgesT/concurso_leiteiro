class Produtor:

	def __init__(self, numero, nome, municipio, fazenda, nome_vaca, ordenhas, perc_gordura):
		self.numero = numero
		self.nome = nome
		self.municipio = municipio
		self.fazenda = fazenda
		self.nome_vaca = nome_vaca
		self.ordenhas = ordenhas
		self.perc_gordura = perc_gordura


class Concurso:

	def __init__(self, numero, localidade, categoria, n_dias_ordenha, produtores):
		self.numero = numero
		self.localidade = localidade
		self.categoria = categoria
		self.n_dias_ordenha = n_dias_ordenha
		self.produtores = produtores


	def appendProdutor(self, novo_produtor):
		self.produtores.append(novo_produtor)

