from queue import PriorityQueue

initial_state = (3, 3, 1)
goal_state = (0, 0, 0)
MISSIONARY_COST = 10
CANNIBAL_COST = 20

def is_valid_state(state):
    missionaries_left, cannibals_left, boat_position = state

    if missionaries_left < 0 or cannibals_left < 0 or missionaries_left > 3 or cannibals_left > 3:
        return False

    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False

    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False

    return True

def uniform_cost_search():
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    visited = set()

    while not frontier.empty():
        cost, state = frontier.get()

        if state == goal_state:
            return cost

        if state not in visited:
            visited.add(state)

            missionaries_left, cannibals_left, boat_position = state

            for m in range(3):
                for c in range(3):
                    if 1 <= m + c <= 2:
                        if boat_position == 1:
                            new_state = (missionaries_left - m, cannibals_left - c, 0)
                        else:
                            new_state = (missionaries_left + m, cannibals_left + c, 1)

                        if is_valid_state(new_state):
                            move_cost = m * MISSIONARY_COST + c * CANNIBAL_COST
                            new_cost = cost + move_cost
                            frontier.put((new_cost, new_state))

    return None

cost = uniform_cost_search()

if cost is not None:
    print("Minimum cost to cross the river:", cost)
else:
    print("Solution not found.")
