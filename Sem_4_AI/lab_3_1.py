import pandas as pd
myData = {
    'Std_Name': ['Bharath', 'Jignesh', 'Divyagnan', 'Sivamani', 'Chetana', 'Pranav', 'Satvik', 'Sriniketh'],
    'Roll_No': [55, 56, 130, 144, 169, 213, 221, 226],
    'CPI': [74, 81, 64, 37, 54, 69, 81, 66]
}

myDataFrame = pd.DataFrame(myData)

print("My total data:")
print(myDataFrame)
print("---------------------------------------------------------------------------------------------")

reqDataFrame = myDataFrame[myDataFrame['CPI'] > 60]
print("Updated Data Frame:")
print(reqDataFrame)
print("---------------------------------------------------------------------------------------------")

mean = myDataFrame['CPI'].mean()
median = myDataFrame['CPI'].median()
std_dev = myDataFrame['CPI'].std()

print("Mean: " + str(mean))
print("Median: " + str(median))
print("Standard Deviation: " + str(std_dev))