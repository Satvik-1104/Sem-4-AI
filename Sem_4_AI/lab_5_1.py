import heapq
import copy


class PuzzleNode:
    def __init__(self, puzzle, parent=None, move=""):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.depth = 0
        self.cost = 0

        if parent:
            self.depth = parent.depth + 1

    def __lt__(self, other):
        return (self.cost + self.depth) < (other.cost + other.depth)

    def __eq__(self, other):
        return self.puzzle == other.puzzle


def h_manhattan(puzzle, goal):
    total_distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                goal_pos = next((r, c) for r, row in enumerate(goal) for c, value in enumerate(row) if value == puzzle[i][j])
                total_distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return total_distance


def get_neighbors(node):
    neighbors = []
    i, j = next((i, j) for i, row in enumerate(node.puzzle) for j, value in enumerate(row) if value == 0)

    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + move[0], j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_puzzle = copy.deepcopy(node.puzzle)
            new_puzzle[i][j], new_puzzle[new_i][new_j] = new_puzzle[new_i][new_j], new_puzzle[i][j]
            neighbors.append(PuzzleNode(new_puzzle, node, move))

    return neighbors


def solve_puzzle(initial_state, goal_state, heuristic):
    start_node = PuzzleNode(initial_state)
    goal_node = PuzzleNode(goal_state)

    if heuristic == "manhattan":
        start_node.cost = h_manhattan(start_node.puzzle, goal_node.puzzle)
    else:
        raise ValueError("Invalid heuristic")

    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.puzzle == goal_node.puzzle:
            path = []
            while current_node.parent:
                path.append(current_node.move)
                current_node = current_node.parent
            path.reverse()
            return path

        closed_set.add(current_node)

        for neighbor in get_neighbors(current_node):
            if neighbor not in closed_set:
                neighbor.cost = h_manhattan(neighbor.puzzle, goal_node.puzzle)
                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)

    return None


# ... (other parts of the code remain unchanged)

if __name__ == "__main__":
    initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    goal = goal_state

    print("Initial State:")
    for row in initial_state:
        print(row)

    print("\nGoal State:")
    for row in goal_state:
        print(row)

    print("\nSolving with A* using Manhattan Distance Heuristic:")
    a_star_solution = solve_puzzle(initial_state, goal_state, heuristic="manhattan")
    print("A* Solution:", a_star_solution)

    # You can also solve it using Greedy Best-First Search by setting the heuristic accordingly.
    # For example:
    # print("\nSolving with Greedy Best-First Search using Manhattan Distance Heuristic:")
    # greedy_solution = solve_puzzle(initial_state, goal_state, heuristic="manhattan")
    # print("Greedy Solution:", greedy_solution)
