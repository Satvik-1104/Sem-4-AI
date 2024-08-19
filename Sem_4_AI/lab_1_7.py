myDictionary = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(myDictionary)

print("The Keys: ")
for keys, values in myDictionary.items():
    print(keys, end=", ")
print()
print("The Values: ")
for keys, values in myDictionary.items():
    print(values, end=", ")
print()
print(myDictionary[list(myDictionary.keys())[1]])