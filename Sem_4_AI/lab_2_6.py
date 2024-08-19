import numpy as np

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

matrix = [[int(input()) for j in range(n)] for i in range(m)]

print("The original matrix is: ")
org_matrix = np.array(matrix)
print(org_matrix)

print("The transpose matrix is: ")
t_matrix = np.transpose(org_matrix)
print(t_matrix)

print("The flattened matrix is: ")
f_matrix = t_matrix.flatten()
print(f_matrix)