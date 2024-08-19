import numpy as np
import random
import math


def calculate_total_distance(tour, distances):
    total_distance = 0
    num_cities = len(tour)
    for i in range(num_cities):
        total_distance += distances[tour[i % num_cities], tour[(i + 1) % num_cities]]
    return total_distance


def generate_initial_solution(num_cities):
    return list(range(num_cities))


def swap_cities(tour):
    tour_copy = tour.copy()
    i, j = random.sample(range(len(tour)), 2)
    tour_copy[i], tour_copy[j] = tour_copy[j], tour_copy[i]
    return tour_copy


def simulated_annealing(distances, initial_temperature, cooling_rate, num_iterations):

    num_cities = len(distances)
    current_tour = generate_initial_solution(num_cities)
    current_distance = calculate_total_distance(current_tour, distances)
    best_tour = current_tour
    best_distance = current_distance

    for iteration in range(num_iterations):
        temperature = initial_temperature * math.exp(-cooling_rate * iteration)

        new_tour = swap_cities(current_tour)
        new_distance = calculate_total_distance(new_tour, distances)

        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_tour = new_tour
            current_distance = new_distance

        if current_distance < best_distance:
            best_tour = current_tour
            best_distance = current_distance

    return best_tour, best_distance


if __name__ == "__main__":
    # Example: Define distances between cities
    cities = ["A", "B", "C", "D"]
    distances = np.array([
        [0, 2, 9, 10],
        [2, 0, 6, 4],
        [9, 6, 0, 8],
        [10, 4, 8, 0]
    ])

    # Experiment with different parameters
    initial_temperature = 1000
    cooling_rate = 0.001
    num_iterations = 10000

    # Run the simulated annealing algorithm
    best_tour, best_distance = simulated_annealing(distances, initial_temperature, cooling_rate, num_iterations)

    # Print the results
    print("Best Tour:", best_tour)
    print("Best Distance:", best_distance)
