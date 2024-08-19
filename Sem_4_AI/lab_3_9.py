import numpy as np
import random

n = int(input("Enter the size of your linear equations: "))
A = np.random.rand(n, n)
b = np.random.rand(n)
x = np.linalg.solve(A, b)

print("A: ")
print(A)

print("b: ")
print(b)

print("x: ")
print(x)