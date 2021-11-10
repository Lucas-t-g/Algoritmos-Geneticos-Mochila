from random import randint, random, choice
from operator import add, mul
from functools import reduce
from numpy import multiply

def geraItens(n=20, peso_min=1, peso_max=10, valor_min=1, valor_max=20):
    itens_pesos = []
    for item_peso in range(n):
        item = {
            "peso": randint(peso_min, peso_max),
            "valor": randint(valor_min, valor_max)
        }
        itens_pesos.append( item )
    return itens_pesos


def individual(length, min, max):
    'Create a member of the population.'
    return [ randint(min,max) for x in range(length) ]

def population(count, length, min, max):
    """
    Create a number of individuals (i.e. a population).

    count: the number of individuals in the population
    length: the number of values per individual
    min: the minimum possible value in an individual's list of values
    max: the maximum possible value in an individual's list of values

    """
    return [ individual(length, min, max) for x in range(count) ]

def fitness(individual, itens, target):
    """
    Determine the fitness of an individual. Higher is better.

    individual: the individual to evaluate
    target: the target number individuals are aiming for

    O fitness do individuo perfeito sera ZERO, ja que o somatorio dara o target
    reduce: reduz um vetor a um escalar, neste caso usando o operador add
    """

    peso_itens = [ item["peso"] for item in itens ]
    valor_itens = [ item["valor"] for item in itens ]

    peso_total = reduce(add, multiply(individual, peso_itens), 0)
    valor_total = reduce(add, multiply(individual, valor_itens), 0)

    # print(individual)
    # print(itens)
    # print(peso_itens)
    # print(valor_itens)
    # print(peso_total)
    # print(valor_total)
    # print(sum)

    if peso_total > target:
        # print("peso demais")
        return 0
    else:
        # print("ok")
        return valor_total

def media_fitness(pop, target, itens):
    'Find average fitness for a population.'
    summed = reduce(add, (fitness(x, itens, target) for x in pop))
    return summed / (len(pop) * 1.0)

def roleta(graded):
    tickets =[]
    for i, score, individual in graded:
        # print([individual]*score)
        tickets += [individual]*(1+score)
    return tickets


def evolve_roleta(pop, target, itens, retain=0.2, random_select=0.05, mutate=0.01):
    'Tabula cada individuo e o seu fitness'
    graded = [ (i, fitness(x, itens, target), x) for i, x in enumerate(pop)]

    'Ordena pelo fitness os individuos - maior->menor'
    graded = sorted(graded, reverse=True)  #inverter a ordem do 'sorted'

    'roleta'
    tickets = roleta(graded)
    retain_length = int(len(graded)*retain)
    parents = []
    while len(parents) < retain_length:
        picked = choice(tickets)
        parents.append(picked)
        while picked in tickets: tickets.remove(picked)

    # randomly add other POUCOS individuals to
    # promote genetic diversity
    while len(parents) < 2: # com uma população pequena é provavel que acabe encontrando um unico pai, então isso garente que hajam pelo menos dois pais
        for individual in graded[retain_length:]:
            if random_select > random():
                parents.append(individual)

    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = randint(
                min(individual), max(individual))
    # crossover parents to create children
    parents_length = len(parents)
    'descobre quantos filhos terao que ser gerados alem da elite e aleatorios'
    desired_length = len(pop) - parents_length
    children = []
    'comeca a gerar filhos que faltam'
    while len(children) < desired_length:
        'escolhe pai e mae no conjunto de pais'
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) // 2
            'gera filho metade de cada'
            child = male[:half] + female[half:]
            'adiciona novo filho a lista de filhos'
            children.append(child)
    'adiciona a lista de pais (elites) os filhos gerados'
    parents.extend(children)
    return parents