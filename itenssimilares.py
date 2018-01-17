from recomendacao import *

#recomendação baseada em usuários
#print(getRecomendacoesUsuarios(avaliacoesUsuarios,'Leonardo'))

#recomendação baseada em itens
itensSimilares = calcularItensSimilares(avaliacoesFilme)

print(getRecomendacoesItens(avaliacoesUsuarios,itensSimilares,'Leonardo'))

