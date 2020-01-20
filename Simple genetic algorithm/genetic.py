import string
import random
from fractions import Fraction
from math import ceil


def create_population(pop_size, chrom_size):
    population = []

    for i in range(0, pop_size):
        population.append(create_chromosome(chrom_size))
    return population


def selection(population, answer):
    GRADED_RETAIN_PERCENT = 0.3
    NONGRADED_RETAIN_PERCENT = 0.2
    score_list = []
    selected = []

    for i in range(0, len(population)):
        score_list.append(score(population[i], answer))

    tuples = sorted(zip(score_list, population), reverse=True)
    sorted_chromosomes = [chromosomes_list for (score_list, chromosomes_list) in tuples]
    print("Best match this generation:", sorted_chromosomes[0])
    while len(selected) < ceil(len(population) * GRADED_RETAIN_PERCENT):
        selected.append(sorted_chromosomes[0])
        sorted_chromosomes.pop(0)

    for i in range(0, ceil(len(population) * NONGRADED_RETAIN_PERCENT)):
        selected.append(random.choice(sorted_chromosomes))
    return selected


def generation(population, answer):
    select = selection(population, answer)
    children = []

    for i in range(0, len(select) + 1):
        parent1 = select[random.randrange(len(select))]
        parent2 = select[random.randrange(len(select))]

        while (parent1 == parent2):
            parent2 = select[random.randrange(len(select))]

        child = crossover(parent1, parent2)
        child = mutation(child)
        children.append(child)

    for child in children:
        select.append(child)
    return select


def crossover(parent1, parent2):
    parent1 = parent1[0:len(parent1)//2]
    parent2 = parent2[len(parent2)//2:len(parent2)]
    child = parent1 + parent2
    return child


def mutation(chrom):
    position = random.randrange(0, len(chrom))
    chrom = chrom[0:position] + get_letter() + chrom[position + 1:len(chrom)]
    return chrom


def create_chromosome(size):
    chromosome = ""
    for i in range(0, size):
        chromosome += get_letter()
    return chromosome


def get_letter():
    alphabet = string.ascii_letters
    return random.choice(alphabet)


def score(chrom, answer):
    count = 0
    point = Fraction(1, len(answer))

    for i in range(0, len(answer)):
        if chrom[i] == answer[i]:
            count += point
    return count


answer = input("Defina uma string de letras maiúsculas e minúsculas para ser encontrada através do algoritmo: ")
chrom_size = len(answer)
population_size = 12
population = create_population(population_size, chrom_size)

while True:
    population = generation(population, answer)

    for chrom in population:
        if chrom == answer:
            print("A string inserida foi:", chrom)
            quit()