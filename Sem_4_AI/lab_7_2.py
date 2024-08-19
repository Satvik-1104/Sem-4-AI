import random

N = 50
K = 5
POPULATION_SIZE = 100
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1

def generate_initial_population():
    return [[random.randint(0, K-1) for _ in range(N)] for _ in range(POPULATION_SIZE)]

def fitness_function(individual):
    group_diversities = [0] * K
    group_counts = [0] * K
    for i, group in enumerate(individual):
        group_diversities[group] += i
        group_counts[group] += 1
    return sum(diversity / count if count > 0 else 0 for diversity, count in zip(group_diversities, group_counts))

def select_parents(population, fitness_values, tournament_size=3):
    selected_parents = []
    for _ in range(2):
        tournament = random.sample(list(zip(population, fitness_values)), k=tournament_size)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected_parents.append(winner)
    return selected_parents

def crossover(parent1, parent2):
    crossover_point = random.randint(1, N-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual):
    mutated_individual = individual[:]
    student_to_mutate = random.randint(0, N-1)
    mutated_individual[student_to_mutate] = random.randint(0, K-1)
    return mutated_individual

def genetic_algorithm():
    population = generate_initial_population()
    for _ in range(NUM_GENERATIONS):
        fitness_values = [fitness_function(individual) for individual in population]
        next_generation = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = select_parents(population, fitness_values)
            offspring1, offspring2 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1) if random.random() < MUTATION_RATE else offspring1
            offspring2 = mutate(offspring2) if random.random() < MUTATION_RATE else offspring2
            next_generation.extend([offspring1, offspring2])
        population = next_generation
    best_solution = max(population, key=fitness_function)
    return best_solution

def main():
    best_solution = genetic_algorithm()
    group_assignments = {}
    for i, group in enumerate(best_solution):
        if group not in group_assignments:
            group_assignments[group] = []
        group_assignments[group].append(i)

    for group, students in group_assignments.items():
        print(f"Group {group + 1}: {students}, Diversity: {len(students)}")

if __name__ == "__main__":
    main()

