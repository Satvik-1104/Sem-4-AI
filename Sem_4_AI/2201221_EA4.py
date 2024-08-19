import random


class Game:
    def __init__(self):
        self.stones = 50
        self.player = random.choice(['AI', 'Human'])

    def make_move(self, move):
        self.stones -= move

    def is_game_over(self):
        return self.stones <= 0

    def get_valid_moves(self):
        return [1, 2] if self.stones >= 2 else [1]


def evaluate(state):
    return -state.stones


def minimax(node, depth, isMaximizingPlayer, alpha, beta):
    if node.is_game_over() or depth == 0:
        return evaluate(node)

    if isMaximizingPlayer:
        bestVal = float('-inf')
        for move in node.get_valid_moves():
            node.make_move(move)
            value = minimax(node, depth - 1, False, alpha, beta)
            node.make_move(-move)
            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal
    else:
        bestVal = float('inf')
        for move in node.get_valid_moves():
            node.make_move(move)
            value = minimax(node, depth - 1, True, alpha, beta)
            node.make_move(-move)
            bestVal = min(bestVal, value)
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        return bestVal


def alpha_beta_search(state, depth, isMaximizingPlayer, alpha, beta):
    if state.is_game_over() or depth == 0:
        return evaluate(state)

    if isMaximizingPlayer:
        bestVal = float('-inf')
        for move in state.get_valid_moves():
            state.make_move(move)
            value = alpha_beta_search(state, depth - 1, False, alpha, beta)
            state.make_move(-move)
            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal
    else:
        bestVal = float('inf')
        for move in state.get_valid_moves():
            state.make_move(move)
            value = alpha_beta_search(state, depth - 1, True, alpha, beta)
            state.make_move(-move)
            bestVal = min(bestVal, value)
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        return bestVal

def alpha_beta_search_wrapper(state, depth):
    alpha = float('-inf')
    beta = float('inf')
    best_move = None
    for move in state.get_valid_moves():
        state.make_move(move)
        eval = alpha_beta_search(state, depth - 1, False, alpha, beta)
        state.make_move(-move)
        if eval > alpha:
            alpha = eval
            best_move = move
    return best_move


def main():
    game = Game()
    print("Initial stones:", game.stones)
    print("First turn:", game.player)

    while not game.is_game_over():
        if game.player == 'AI':
            move = alpha_beta_search_wrapper(game, 50)
            print("AI removes", move, "stones.")
        else:
            move = int(input("Your turn. Enter 1 or 2: "))
        game.make_move(move)
        print("Stones left:", game.stones)
        game.player = 'Human' if game.player == 'AI' else 'AI'

    winner = 'AI' if game.player == 'Human' else 'Human'
    print("Game over. Winner is", winner)


if __name__ == "__main__":
    main()
