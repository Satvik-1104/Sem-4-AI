from queue import Queue


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()


def is_goal(board, goal):
    return board == goal


def get_blank_position(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == 0:
                return i, j


def generate_successors(board):
    successors = []
    blank_i, blank_j = get_blank_position(board)

    for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_i, new_j = blank_i + move[0], blank_j + move[1]

        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_board = [row[:] for row in board]
            new_board[blank_i][blank_j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[blank_i][blank_j]
            successors.append(new_board)

    return successors


def bfs(start, goal):
    visited = set()
    queue = Queue()

    queue.put((start, []))

    while not queue.empty():
        current_board, path = queue.get()
        visited.add(tuple(map(tuple, current_board)))

        if is_goal(current_board, goal):
            return path

        for successor in generate_successors(current_board):
            if tuple(map(tuple, successor)) not in visited:
                queue.put((successor, path + [successor]))

    return None

if __name__ == "__main__":
    # Example initial and goal states
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    print("Initial state:")
    print_board(initial_state)

    print("Goal state:")
    print_board(goal_state)

    solution_path = bfs(initial_state, goal_state)

    if solution_path:
        print("Solution path:")
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}:")
            print_board(state)
    else:
        print("No solution found.")
