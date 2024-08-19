import random
import numpy as np

m = random.randint(1, 50)
n = random.randint(1, 50)

matrix = np.random.randint(1, 50, size=(m, n))
print(matrix)
print("the second element of the last row is: ")
print(matrix[-1, 1])