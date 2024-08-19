from collections import deque

def water_jug_bfs(Jug1_capacity, Jug2_capacity, target_amount):
    visited = set()
    queue = deque([((0, 0), [])])  # Each queue element is a tuple containing state and steps

    while queue:
        current_state, steps = queue.popleft()
        jug1_water, jug2_water = current_state

        if jug1_water == target_amount or jug2_water == target_amount:
            return steps + [current_state]

        next_states = []

        next_states.append(((Jug1_capacity, jug2_water), steps + [current_state, f"Fill jug 1"]))
        next_states.append(((jug1_water, Jug2_capacity), steps + [current_state, f"Fill jug 2"]))
        next_states.append(((0, jug2_water), steps + [current_state, f"Empty jug 1"]))
        next_states.append(((jug1_water, 0), steps + [current_state, f"Empty jug 2"]))
        next_states.append(((jug1_water - min(jug1_water, Jug2_capacity - jug2_water), jug2_water + min(jug1_water, Jug2_capacity - jug2_water)), steps + [current_state, f"Pour from jug 1 to jug 2"]))
        next_states.append(((jug1_water + min(Jug1_capacity - jug1_water, jug2_water), jug2_water - min(Jug1_capacity - jug1_water, jug2_water)), steps + [current_state, f"Pour from jug 2 to jug 1"]))

        for state, step in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, step))

    return None

Jug1_capacity = int(input("Enter the capacity of jug 1: "))
Jug2_capacity = int(input("Enter the capacity of jug 2: "))
target_amount = int(input("Enter the target amount: "))
result = water_jug_bfs(Jug1_capacity, Jug2_capacity, target_amount)

if result:
    print(f"Target amount {target_amount} litres can be measured with the following steps:")
    for step in result[1:]:
        print(step)
else:
    print("Target amount cannot be measured with the given jug capacities.")
