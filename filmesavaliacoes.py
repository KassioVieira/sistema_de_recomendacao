avaliacoes = {'Freddy x Jason': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Pedro': 2.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0 },
	 
	 'O Ultimato Bourne': 
		{'Ana': 3.5, 
		 'Marcos': 3.5,
		 'Pedro': 3.0, 
		 'Claudia': 3.5, 
		 'Adriano': 4.0, 
		 'Janaina': 4.0,
		 'Leonardo': 4.5 },
				 
	 'Star Trek': 
		{'Ana': 3.0, 
		 'Marcos:': 1.5,
		 'Claudia': 3.0, 
		 'Adriano': 2.0 },
	
	 'Exterminador do Futuro': 
		{'Ana': 3.5, 
		 'Marcos:': 5.0 ,
		 'Pedro': 3.5, 
		 'Claudia': 4.0, 
		 'Adriano': 3.0, 
		 'Janaina': 5.0,
		 'Leonardo': 4.0},
				 
	 'Norbit': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Claudia': 2.5, 
		 'Adriano': 2.0, 
		 'Janaina': 3.5,
		 'Leonardo': 1.0},
				 
	 'Star Wars': 
		{'Ana': 3.0, 
		 'Marcos:': 3.5,
		 'Pedro': 4.0, 
		 'Claudia': 4.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0}
}

from math import sqrt

def euclidiana(usuario1, usuario2):
	si = {}
	for item in avaliacoes[usuario1]:
		if item in avaliacoes[usuario2]: si[item] = 1
	if len(si) == 0: return 0

	soma = sum([pow(avaliacoes[usuario1][item]  - avaliacoes[usuario2][item], 2)
				for item in avaliacoes[usuario1] if item in avaliacoes[usuario2]])

	return 1/(1+ sqrt(soma))


def getSimilares(usuario):
	similaridade = [(euclidiana(usuario, outro), outro)
					for outro in avaliacoes if outro != usuario]
	similaridade.sort()
	similaridade.reverse()
	return similaridade

def getRecomendacoes(usuario):
	totais  = {}
	somaSimilaridade = {}
	for outro in avaliacoes:
		if outro == usuario: continue
		similaridade = euclidiana(usuario,outro)

		if similaridade <= 0: continue

		for item in avaliacoes[outro]:
			if item not in avaliacoes[usuario]:
				totais.setdefault(item, 0)
				totais[item] += avaliacoes[outro][item] * similaridade
				somaSimilaridade.setdefault(item, 0)
				somaSimilaridade[item] += similaridade
	
	rankings = [(total / somaSimilaridade[item], item) for item, total in totais.items()]
	rankings.sort()
	rankings.reverse()
	return rankings