from recomendacao import *

#print(euclidiana(avaliacoesUsuarios,'Leonardo','Ana'))
#print(euclidiana(avaliacoesFilme,'Star Wars','Star Trek'))

#print(getSimilares(avaliacoesUsuarios,'Pedro'))

#print(getSimilares(avaliacoesFilme,'Star Wars'))

#print(getRecomendacoes(avaliacoesUsuarios,'Leonardo'))

#print(getRecomendacoes(avaliacoesFilme,'Star Wars'))

#carregaMovieLens()
base = carregaMovieLens()
#print(getSimilares(base,'212'))
#print(getSimilares(base, '1'))
print(getRecomendacoes(base,'1'))