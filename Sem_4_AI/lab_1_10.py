n = int(input("Enter the size of the list: "))
print("Enter the numbers: ")
myList = [int(input()) for i in range(n)]
print(set(myList))