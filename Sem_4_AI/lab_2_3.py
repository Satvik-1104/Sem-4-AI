import os

str = "This line has been appended in the text file using python code"
with open('text.txt', 'a') as file:
    file.write(str)
file.close()

with open('text.txt', 'r') as file:
    print(file.read())
file.close()