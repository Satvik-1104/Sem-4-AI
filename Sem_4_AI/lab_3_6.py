"""import random
import numpy as np
import time


def matrix_multi_loops(matrix_p, matrix_q, rows_a, cols_b, cols_a):
    result_matrix = [
        [0 for i in range(106)] for j in range(106)
    ]
    start_time = time.time()
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result_matrix[i][j] += matrix_p[i][k] * matrix_q[k][j]
    end_time = time.time()
    result_matrix = np.array(result_matrix)
    print(result_matrix)
    time_taken = end_time - start_time
    return time_taken


def matrix_multi_vector(matrix_p, matrix_q):
    start_time = time.time()
    result_matrix = np.dot(matrix_p, matrix_q)
    end_time = time.time()
    print(result_matrix)
    time_taken = end_time - start_time
    return time_taken


matrix_P = np.random.randint(1, 200, size=(106, 104))
matrix_Q = np.random.randint(1, 200, size=(106, 104))
matrix_Qt = np.transpose(matrix_Q)

print("Matrix P:")
print(matrix_P)
print("--------------------------------------------------------------------------------------")

print("Matrix Q:")
print(matrix_Q)
print("--------------------------------------------------------------------------------------")

print("The product matrix is (P * Q transpose): ")
time_taken1 = matrix_multi_loops(matrix_P, matrix_Qt, 106, 106, 104)
print()
print("The time taken to multiply using loops is " + str(time_taken1) + "s")
print("--------------------------------------------------------------------------------------")

print("The product matrix is (P * Q transpose): ")
time_taken2 = matrix_multi_vector(matrix_P, matrix_Qt)
print()
print("The time taken to multiply using vectorized multiplication is " + str(time_taken2) + "s")
print("--------------------------------------------------------------------------------------")

speedup = time_taken1/time_taken2
print("Speed up is: " + str(speedup))"""

import numpy as np
import time
import random

def m_mul_loops(matrix_p, matrix_qt, rows_a, cols_b, cols_a):
    p_matrix = [[0 for a in range(106)] for b in range(106)]
    start_time = time.time()
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                p_matrix[i][j] += matrix_p[i][k] * matrix_qt[k][j]
    end_time = time.time()
    result_matrix = np.array(p_matrix)
    print("Loops product: ")
    print(result_matrix)
    time_taken = end_time - start_time
    return time_taken

def v_mul (matrix_p, matrix_qt):
    start_time = time.time()
    p_matrix = np.dot(matrix_p, matrix_qt)
    end_time = time.time()
    print("Vector product: ")
    print(p_matrix)
    time_taken = end_time - start_time
    return time_taken

mp = np.random.randint(1, 200, size=(106, 104))
mq = np.random.randint(1, 200, size=(106, 104))
mqt = np.transpose(mq)
print("Matrix P:")
print(mp)
print("Matrix Q:")
print(mq)
print("Matrix Q transpose:")
print(mqt)
loops_time = m_mul_loops(mp, mqt, 106, 106, 104)
vector_mul_time = v_mul(mp, mqt)
print("Loops time: ")
print(str(loops_time))
print()
print("Vector mul time: ")
print(str(vector_mul_time))
print("Speed up: " + str(loops_time / vector_mul_time))