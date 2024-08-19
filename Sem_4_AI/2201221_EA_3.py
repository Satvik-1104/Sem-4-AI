import random
import math

def calculate_diversity(groups):
    diversity = 0
    for group in groups:
        marks = [student[1] for student in group]
        mean = sum(marks) / len(marks)
        diversity += sum((mark - mean) ** 2 for mark in marks)
    return diversity

def stochastic_hill_climbing(students, k, max_iterations=1000, alpha=0.5):
    groups = [[] for _ in range(k)]
    for student in students:
        random.choice(groups).append(student)

    current_diversity = calculate_diversity(groups)
    best_diversity = current_diversity
    best_groups = [group[:] for group in groups]

    for _ in range(max_iterations):
        if not students:
            break

        i = random.randint(0, len(students) - 1)
        j = random.randint(0, k - 1)
        new_groups = [group[:] for group in groups]
        new_groups[j].append(students[i])

        students.pop(i)

        new_diversity = calculate_diversity(new_groups)

        # Ensure diversity decreases
        if new_diversity < current_diversity:
            groups = new_groups
            current_diversity = new_diversity

            if current_diversity < best_diversity:
                best_diversity = current_diversity
                best_groups = [group[:] for group in groups]
        else:
            # Reinsert the removed student if the move is rejected
            students.insert(i, new_groups[j][-1])

    return best_groups


N = 10
k = 3
students = [(f"Student {i}", random.randint(0, 100)) for i in range(N)]

for student in students:
    print(student[0]+": "+str(student[1]))
# Sort students by marks (ascending order) before passing to the algorithm
students.sort(key=lambda x: x[1])

best_groups = stochastic_hill_climbing(students, k)
for i, group in enumerate(best_groups):
    print(f"Group {i+1}: {', '.join([student[0] for student in group])}")
