import numpy as np
import random
import time

# Define the distance matrix (assuming symmetric distances)
# Example distance matrix for 5 cities
distance_matrix = np.array([
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 40],
    [25, 30, 20, 40, 0]
])

# Define parameters
num_cities = len(distance_matrix)
population_size = 50
mutation_rate = 0.1
num_generations = 1000

# Create random initial population
def create_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population

# Calculate total distance of a route
def calculate_distance(route, distance_matrix):
    distance = 0
    for i in range(len(route) - 1):
        distance += distance_matrix[route[i]][route[i+1]]
    distance += distance_matrix[route[-1]][route[0]]  # Return to starting city
    return distance

# Crossover operator (order crossover)
def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start + 1, len(parent1))
    child = [-1] * len(parent1)
    for i in range(start, end):
        child[i] = parent1[i]
    j = 0
    for i in range(len(parent2)):
        if parent2[i] not in child:
            while child[j] != -1:
                j += 1
            child[j] = parent2[i]
    return child

# Mutation operator (swap mutation)
def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]
    return individual

# Genetic algorithm
# Genetic algorithm
def genetic_algorithm(distance_matrix, population_size, mutation_rate, num_generations):
    start_time = time.time()
    population = create_population(population_size, num_cities)
    for generation in range(num_generations):
        # Selection: tournament selection
        selected = random.sample(population, population_size)
        selected.sort(key=lambda x: calculate_distance(x, distance_matrix))
        # Crossover
        offspring = []
        for i in range(0, len(selected), 2):
            offspring.append(crossover(selected[i], selected[i+1]))
        # Mutation
        mutated_offspring = [mutate(individual, mutation_rate) for individual in offspring]
        # Replacement: elitism (keep the best individuals)
        population = selected[:population_size // 2] + mutated_offspring
    best_route = min(population, key=lambda x: calculate_distance(x, distance_matrix))
    best_distance = calculate_distance(best_route, distance_matrix)
    end_time = time.time()
    computational_time = end_time - start_time
    return best_route, best_distance, computational_time


# Run the genetic algorithm
best_route, best_distance, computational_time = genetic_algorithm(distance_matrix, population_size, mutation_rate, num_generations)

# Print the results
print("Best route:", best_route)
print("Best distance:", best_distance)
print("Computational time:", computational_time, "seconds")
