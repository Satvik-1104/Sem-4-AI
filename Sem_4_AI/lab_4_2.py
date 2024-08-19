def find_occurence(num_list, target):
    for i in range(len(num_list)):
        if num_list[i] == target:
            return i
    return -1

n = int(input("Enter the size of the array: "))
print("Enter the elements of the list: ")
myList = [int(input()) for i in range(n)]
print(myList)
t = int(input("Enter the target element: "))
print()
occ_ind = find_occurence(myList, t)
if occ_ind >= 0:
    print(occ_ind)
else:
    print("Not found")