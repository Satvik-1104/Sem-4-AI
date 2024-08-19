import numpy as np

matrix = np.random.randint(1, 10, size=(8,7))
print(matrix)

max = np.max(matrix, axis=0)
min = np.min(matrix, axis=0)

print("The maximum values from each feature are: ")
print(max)

print("The minimum values from each feature are: ")
print(min)