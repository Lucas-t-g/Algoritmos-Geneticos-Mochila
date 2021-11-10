
# Objetivo: achar um vetor de inteiros (entre i_min e i_max) com i_length posicoes cuja a soma de todos os termos seja o mais proximo possivel de target

#O algoritmo rodara epochs vezes -> numero de populacoes geradas. Sera impresso a media de fitness de cada uma das epochs populacoes

#RODAR COM PYTHON 2!!! (senao colocar () em print e tirar x de xrange
  
from genetic2020 import *
target = 20   # quanto de peso pode-se levar na mochila

i_length = 10   # tamanho do cromossomo (quantos itens tem)
i_min = 0       # valor minimo pra cada gene
i_max = 1       # valor máximo pra cada gene
p_count = 20    # quantia de individuos da população
epochs = 300    # número de gerações

itens = [{'peso': 2, 'valor': 20}, {'peso': 4, 'valor': 11}, {'peso': 7, 'valor': 20}, {'peso': 3, 'valor': 18}, {'peso': 10, 'valor': 14}, {'peso': 4, 'valor': 19}, {'peso': 8, 'valor': 13}, {'peso': 5, 'valor': 8}, {'peso': 3, 'valor': 5}, {'peso': 7, 'valor': 10}]
# itens = geraItens(n=i_length)
# print(itens)
# exit()

p = population(p_count, i_length, i_min, i_max)

fitness_history = [media_fitness(p, target, itens),]

for i in range(epochs):
    # print(i)
    p = evolve_roleta(p, target, itens)
    fitness_history.append(media_fitness(p, target, itens))

for datum in fitness_history:
   print (datum)