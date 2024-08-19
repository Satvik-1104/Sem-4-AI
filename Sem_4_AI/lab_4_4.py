def max_between_lists (list1, list2):
    co_max_list = []
    for i in range(0, len(list1)):
        if list1[i] == list2[i]:
            co_max_list.append(list1[i])
        else:
            co_max_list.append(max(list1[i], list2[i]))
    return co_max_list


n = int(input("Enter the size of the Lists: "))
print("Enter " + str(n) + " elements for List 1")
list_1 = [int(input()) for i in range(0, n)]
print("Enter " + str(n) + " elements for List 2")
list_2 = [int(input()) for j in range(0, n)]
print("List 1: ")
print(list_1)
print("List 2: ")
print(list_2)
max_list = max_between_lists(list_1, list_2)
print("The corresponding max list is: ")
print(max_list)