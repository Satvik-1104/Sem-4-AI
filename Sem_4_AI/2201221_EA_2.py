import numpy as np
import random
import time

# Problem parameters
NUM_QUESTIONS = 10
POPULATION_SIZE = 15
CROSSOVER_PROBABILITY = 0.6
MUTATION_PROBABILITY = 0.5
MAX_GENERATIONS = 30

def generate_population(population_size, num_questions):
    return np.random.randint(2, size=(population_size, num_questions))

def fitness(individual):
    return np.sum(individual)

def roulette_wheel_selection(population, fitness_values):
    total_fitness = np.sum(fitness_values)
    probabilities = fitness_values / total_fitness
    return random.choices(population, weights=probabilities)[0]

def multi_point_crossover(parent1, parent2):
    crossover_points = sorted(random.sample(range(NUM_QUESTIONS - 1), 2))
    child1 = np.concatenate((parent1[:crossover_points[0]], parent2[crossover_points[0]:crossover_points[1]], parent1[crossover_points[1]:]))
    child2 = np.concatenate((parent2[:crossover_points[0]], parent1[crossover_points[0]:crossover_points[1]], parent2[crossover_points[1]:]))
    return child1, child2

def bit_flip_mutation(individual):
    mutation_points = random.sample(range(NUM_QUESTIONS), int(MUTATION_PROBABILITY * NUM_QUESTIONS))
    for point in mutation_points:
        individual[point] = 1 - individual[point]
    return individual

def genetic_algorithm():
    population = generate_population(POPULATION_SIZE, NUM_QUESTIONS)
    for generation in range(MAX_GENERATIONS):
        # Evaluate fitness
        fitness_values = np.array([fitness(individual) for individual in population])

        # Selection
        selected_population = [roulette_wheel_selection(population, fitness_values) for _ in range(POPULATION_SIZE)]

        # Crossover
        offspring_population = []
        for i in range(0, POPULATION_SIZE - 1, 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i + 1]
            if random.random() < CROSSOVER_PROBABILITY:
                child1, child2 = multi_point_crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            offspring_population.extend([child1, child2])

        # Mutation
        mutated_population = [bit_flip_mutation(individual) for individual in offspring_population]

        population = mutated_population

    # Find best solution
    best_solution = max(population, key=fitness)
    best_fitness = fitness(best_solution)
    return best_solution, best_fitness

if __name__ == "__main__":
    start_time = time.time()
    best_solution, best_fitness = genetic_algorithm()
    end_time = time.time()

    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)
    print("Computational Time:", end_time - start_time, "seconds")
