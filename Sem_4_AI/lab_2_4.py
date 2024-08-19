import os

total_count = 0
count = 0
with open('test_file.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        total_count += 1
        if not line.startswith('T'):
            count += 1
print("The total number of lines are: " + str(total_count))
print("The lines not starting with 'T' are " + str(count))