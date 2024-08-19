import numpy as np

n = np.random.randint(1, 10)
m = np.random.randint(1, 10)

matrix_1 = np.random.randint(1, 20, size=(m, n))
matrix_2 = np.random.randint(1, 20, size=(m, n))

print("Matrix 1: ")
print(matrix_1)
print("Matrix 2: ")
print(matrix_2)

con_matrix = np.concatenate((matrix_1, matrix_2), axis=1)
print("The concatenated matrix is: ")
print(con_matrix)

print("The sorted 1st array is: ")
sorted_m1 = np.sort(matrix_1, axis=1)
print(sorted_m1)

print("The sorted 2nd array is: ")
sorted_m2 = np.sort(matrix_2, axis=1)
print(sorted_m2)

a_matrix = matrix_1 + matrix_2
print("The addition matrix is: ")
print(a_matrix)

s_matrix = matrix_1 - matrix_2
print("The subtraction matrix is: ")
print(s_matrix)

p_matrix = matrix_1 * matrix_2
print("The product matric is: ")
print(p_matrix)

d_matrix = matrix_1 / matrix_2
print("The division matrix is: ")
print(d_matrix)