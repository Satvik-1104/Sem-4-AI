import numpy as np


def objective_function(x):
    return -x**2 + 8*x


def hill_climbing(initial_x, step_size, range_start, range_end, max_iterations=100):
    current_x = initial_x
    current_value = objective_function(current_x)

    for iteration in range(max_iterations):
        next_x = current_x + step_size
        next_value = objective_function(next_x)

        if next_value > current_value:
            current_x = next_x
            current_value = next_value
        else:
            break

    return current_x, current_value


if __name__ == "__main__":
    initial_values = [-5, 0, 5]
    step_sizes = [0.1, 0.5, 1.0]

    for initial_value in initial_values:
        for step_size in step_sizes:
            result_x, result_value = hill_climbing(initial_value, step_size, -10, 10)
            print(f"Initial Value: {initial_value}, Step Size: {step_size}, Max Value: {result_value:.2f} at x = {result_x:.2f}")
