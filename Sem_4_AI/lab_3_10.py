import numpy as np

scores = [85,92,75,85,90,92,85,75,85,92,75,85,90,92,85,75,85,92]
frequencies = np.bincount(scores)
print("The frequency of 85 is: ")
print(frequencies[85])