import pandas as pd

myData = {
    'Name': ['Bharath', 'Jignesh', 'Divyagnan', 'Sivamani', 'Chetana', 'Pranav', 'Satvik', 'Sriniketh'],
    'Age': [19, 20, 47, 38, 24, 15, 19, 54],
    'Salary': [75000, 81000, -64000, 37000, -54000, 69000, 81000, -90000]
}

dirty_data = pd.DataFrame(myData)
print("Total Data:")
print(dirty_data)
print("---------------------------------------------------------------------------------------------")

index_to_remove = dirty_data[(dirty_data['Age'] < 18) | (dirty_data['Salary'] < 0)].index
dirty_data.drop(index_to_remove, inplace=True)

print("Modified Data:")
print(dirty_data)
print("---------------------------------------------------------------------------------------------")