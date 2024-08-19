import random
import math
import time

N = 8
mutation_probability = float(input("Enter mutation probability: "))


def fitness(board):
    # Calculate the number of attacking pairs of queens
    attacks = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(N), 2))
    child = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    return child

def mutate(child):
    i, j = random.sample(range(N), 2)
    child[i], child[j] = child[j], child[i]
    return child

def genetic_algorithm():
    population_size = 100
    generations = 1000

    population = [random.sample(range(N), N) for _ in range(population_size)]

    for _ in range(generations):
        population.sort(key=lambda x: fitness(x))
        elite = population[:10]  # Elitism: keep top 10 individuals
        offspring = []

        while len(offspring) < population_size - 10:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_probability:  # Mutation rate
                child = mutate(child)
            offspring.append(child)

        population = elite + offspring

    return population[0]


T_initial = float(input("Enter initial temperature: "))
T_final = float(input("Enter final temperature: "))
cooling_rate = float(input("Enter the cooling rate: "))
# Simulated Annealing
def simulated_annealing(T_initial, T_final, cooling_rate):
    def energy(board):
        return fitness(board)

    def random_neighbor(board):
        i, j = random.sample(range(N), 2)
        neighbor = board.copy()
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        return neighbor

    def acceptance_probability(old_energy, new_energy, T):
        return 1.0 if new_energy < old_energy else math.exp((old_energy - new_energy) / T)


    current_solution = random.sample(range(N), N)

    while T_initial > T_final:
        neighbor = random_neighbor(current_solution)
        delta_energy = energy(neighbor) - energy(current_solution)
        if delta_energy < 0 or random.random() < acceptance_probability(energy(current_solution), energy(neighbor), T_initial):
            current_solution = neighbor
        T_initial *= cooling_rate

    return current_solution

if __name__ == "__main__":
    ga_start = time.time()
    ga_solution = genetic_algorithm()
    ga_end = time.time()
    sa_start = time.time()
    sa_solution = simulated_annealing(T_initial, T_final, cooling_rate)
    sa_end = time.time()

    ga_time = ga_end - ga_start
    sa_time = sa_end - sa_start

    print("Genetic Algorithm Solution:", ga_solution)
    print("Time taken is " + str(ga_time))
    print("Simulated Annealing Solution:", sa_solution)
    print("Time taken is " + str(sa_time))
