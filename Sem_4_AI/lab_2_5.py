import os

print("The data in the source file is as follows: ")
with open('source.txt', 'r') as source:
    print(source.read())
source.close()

with open('text.txt', 'r') as source_file:
    with open('destination.txt', 'w') as dest_file:
        dest_file.write(source_file.read())
    dest_file.close()
source_file.close()

print("The content has been copied to the destination file.")
with open('destination.txt', 'r') as destination_file:
    print(destination_file.read())