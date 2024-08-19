def get_water(j1, j2, t):
    if t % j1 == 0:
        print(t//j1 + " times the amount of jug_1")
    elif t % j2 == 0:
        print(t//j2 + " times the amount of jug_2")
    j_diff = max(j1, j2) - min(j1, j2)
    if t % j_diff == 0:
        print(t//j_diff + " times the amount of difference between the 2 jugs")
    j_sum = j1 + j2
    if t % j_sum == 0:
        print(t//j_sum + " times the amount of jug_1")


jug_1 = int(input("Capacity of jug 1: "))
jug_2 = int(input("Capacity of jug 2: "))
target = int(input("Target amount: "))

print("The capacities and the target amount: ")
print("Jug 1: " + str(jug_1))
print("Jug 2: " + str(jug_2))
print("Target: " + str(target))

jug_diff = abs(jug_1 - jug_2)
jug_sum = abs(jug_1 + jug_2)

get_water(jug_1, jug_2, target)