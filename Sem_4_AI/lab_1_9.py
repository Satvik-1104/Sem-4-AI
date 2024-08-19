n = int(input("Enter the size of the list: "))
print("Enter the numbers: ")

myList = [int(input()) for i in range(n)]
for i in myList:
    print(str(i))