import numpy as np
from collections import Counter
import random

array = np.random.randint(1, 30, size=(5, 6))
print(array)
flat_array = array.flatten()
freq_dic = Counter(flat_array)

for numbers, frequency in freq_dic.items():
    if frequency > 1:
        print("Number: " + str(numbers) + "   Frequency: " + str(frequency))