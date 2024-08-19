import random

def fitness_function(x):
    return 2 * x ** 2 + 1

def generate_initial_population(population_size):
    return [random.uniform(0, 6) for _ in range(population_size)]

def evaluate_population(population):
    return [fitness_function(chromosome) for chromosome in population]

def select_parents(population, fitness_values, num_parents):
    selected_parents = []
    for _ in range(num_parents):
        tournament = random.choices(list(zip(population, fitness_values)), k=3)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected_parents.append(winner)
    return selected_parents

def crossover(parent1, parent2):
    return (parent1 + parent2) / 2

def mutate(chromosome, mutation_rate):
    if random.random() < mutation_rate:
        return random.uniform(0, 6)
    return chromosome

def genetic_algorithm(population_size, num_generations, crossover_rate, mutation_rate):
    population = generate_initial_population(population_size)
    for generation in range(num_generations):
        fitness_values = evaluate_population(population)
        parents = select_parents(population, fitness_values, 2)
        next_generation = []
        for i in range(0, population_size, 2):
            offspring = crossover(parents[0], parents[1])
            offspring = mutate(offspring, mutation_rate)
            next_generation.append(offspring)
        population = next_generation
    best_solution = max(population, key=fitness_function)
    return best_solution, fitness_function(best_solution)

best_solution, best_fitness = genetic_algorithm(population_size=50, num_generations=100, crossover_rate=0.8, mutation_rate=0.1)
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
