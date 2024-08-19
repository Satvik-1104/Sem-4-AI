import numpy as np
import random
import math

# Number of students and groups
N = 5
k = 2

# Student marks (example)
student_marks = np.array([85, 70, 90, 60, 80])

# Define the objective function
def objective_function(groups, student_marks):
    diversity = 0
    for group in groups:
        if group:
            group_avg = np.mean(student_marks[group])
            diversity += np.var(student_marks[group])
    return diversity

# Initialize groups randomly
def initialize_groups(N, k):
    groups = [[] for _ in range(k)]
    for i in range(N):
        groups[random.randint(0, k - 1)].append(i)
    return groups

# Simulated Annealing algorithm
def simulated_annealing(student_marks, N, k, initial_temp=1000, cooling_rate=0.95, num_iterations=1000):
    current_groups = initialize_groups(N, k)
    current_diversity = objective_function(current_groups, student_marks)
    best_groups = current_groups
    best_diversity = current_diversity

    current_temp = initial_temp

    for _ in range(num_iterations):
        # Generate a neighboring solution by swapping students between groups
        new_groups = [group.copy() for group in current_groups]
        student_index = random.randint(0, N - 1)
        current_group_index = next((i for i, group in enumerate(current_groups) if student_index in group), None)
        new_group_index = (current_group_index + random.randint(1, k - 1)) % k
        new_groups[current_group_index].remove(student_index)
        new_groups[new_group_index].append(student_index)

        new_diversity = objective_function(new_groups, student_marks)

        # If the new solution is better, accept it
        if new_diversity < current_diversity:
            current_groups = new_groups
            current_diversity = new_diversity
            if new_diversity < best_diversity:
                best_groups = new_groups
                best_diversity = new_diversity
        # If the new solution is worse, accept it with a probability based on the current temperature
        else:
            if random.random() < math.exp(-(new_diversity - current_diversity) / current_temp):
                current_groups = new_groups
                current_diversity = new_diversity

        # Cool down the temperature
        current_temp *= cooling_rate

    return best_groups, best_diversity

# Run simulated annealing
best_groups, best_diversity = simulated_annealing(student_marks, N, k)

# Print the result
print("Best groups:", best_groups)
print("Best diversity:", best_diversity)
