import pandas as pd

myData = {
    'Timestamp': ['2024-02-01 10:56:00', '2024-02-01 16:29:00', '2024-01-31 13:45:17']
}

timestamp = pd.DataFrame(myData)
print("The Timestamp is: ")
print(timestamp)
print("------------------------------------------------------------------------------")

timestamp['Timestamp'] = pd.to_datetime(timestamp['Timestamp'])
timestamp['Hours'] = timestamp['Timestamp'].dt.hour
print("The Timestamp with Hour: ")
print(timestamp)
print("------------------------------------------------------------------------------")