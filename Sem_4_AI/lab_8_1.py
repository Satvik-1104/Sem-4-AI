import random
import math
import time

class Particle:
    def __init__(self, num_students, num_groups):
        self.position = [random.randint(0, num_groups - 1) for _ in range(num_students)]
        self.velocity = [random.uniform(-1, 1) for _ in range(num_students)]
        self.best_position = self.position[:]
        self.best_diversity = float('inf')

def calculate_diversity(groups):
    diversity = 0
    for group in groups:
        if len(group) > 0:
            marks = [student[1] for student in group]
            mean = sum(marks) / len(marks)
            diversity += sum((mark - mean) ** 2 for mark in marks)
    return diversity

def assign_groups(students, positions, k):
    groups = [[] for _ in range(k)]
    for i, group_num in enumerate(positions):
        groups[group_num].append(students[i])
    return groups

def pso_divide_students(students, k, num_particles=30, max_iterations=100, c1=2.0, c2=2.0, w=0.5):
    num_students = len(students)
    particles = [Particle(num_students, k) for _ in range(num_particles)]
    global_best_position = None
    global_best_diversity = float('inf')
    convergence = None
    start_time = time.time()

    for _ in range(max_iterations):
        for particle in particles:
            groups = assign_groups(students, particle.position, k)
            diversity = calculate_diversity(groups)
            if diversity < particle.best_diversity:
                particle.best_position = particle.position[:]
                particle.best_diversity = diversity
            if diversity < global_best_diversity:
                global_best_position = particle.position[:]
                global_best_diversity = diversity
        if convergence is None and global_best_diversity == 0:
            convergence = time.time() - start_time
            break
        for particle in particles:
            for i in range(num_students):
                r1, r2 = random.uniform(0, 1), random.uniform(0, 1)
                particle.velocity[i] = (w * particle.velocity[i] +
                                        c1 * r1 * (particle.best_position[i] - particle.position[i]) +
                                        c2 * r2 * (global_best_position[i] - particle.position[i]))
                particle.position[i] = int(round(particle.position[i] + particle.velocity[i]))
                particle.position[i] = max(min(particle.position[i], k - 1), 0)

    groups = assign_groups(students, global_best_position, k)
    return groups, global_best_diversity, convergence

# Example usage
N = 50
k = 5
students = [(f"Student {i}", random.randint(0, 100)) for i in range(N)]

groups, diversity, convergence = pso_divide_students(students, k)

print("Final Group Assignments and Diversities:")
for i, group in enumerate(groups):
    print(f"Group {i+1}: {', '.join([student[0] for student in group])} - Diversity: {calculate_diversity([group])}")

print("\nOverall Diversity:", diversity)
print("Convergence Time:", convergence)
