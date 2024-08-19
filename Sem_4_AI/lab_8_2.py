import math
import time

class TicTacToe:
    def __init__(self, board=None):
        if board:
            self.board = board
        else:
            self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position):
        self.board[position] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return self.board[i]
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return self.board[i]
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]
        # Check for draw
        if ' ' not in self.board:
            return 'Draw'
        return None

def minimax(game, depth, maximizing_player, verbose=True):
    if game.check_winner() is not None or depth == 0:
        return evaluate(game.board)

    if maximizing_player:
        max_eval = -math.inf
        for move in game.available_moves():
            game.make_move(move)
            eval = minimax(game, depth - 1, False, verbose)
            game.board[move] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in game.available_moves():
            game.make_move(move)
            eval = minimax(game, depth - 1, True, verbose)
            game.board[move] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def alpha_beta_pruning(game, depth, alpha, beta, maximizing_player, verbose=True):
    if game.check_winner() is not None or depth == 0:
        return evaluate(game.board)

    if maximizing_player:
        max_eval = -math.inf
        for move in game.available_moves():
            game.make_move(move)
            eval = alpha_beta_pruning(game, depth - 1, alpha, beta, False, verbose)
            game.board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                if verbose:
                    print("Pruning at depth", depth)
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in game.available_moves():
            game.make_move(move)
            eval = alpha_beta_pruning(game, depth - 1, alpha, beta, True, verbose)
            game.board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                if verbose:
                    print("Pruning at depth", depth)
                break
        return min_eval

def evaluate(board):
    # Evaluation function for Tic-Tac-Toe
    # If 'X' wins, return 1
    # If 'O' wins, return -1
    # If it's a draw, return 0
    # Otherwise, return None
    game = TicTacToe(board)
    winner = game.check_winner()
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif winner == 'Draw':
        return 0
    else:
        return 0  # Return 0 for all other cases

# Example usage
game = TicTacToe()
game.print_board()
print("")

# Minimax
print("Using Minimax:")
minimax_start = time.time()
best_move = None
best_score = -math.inf
for move in game.available_moves():
    game.make_move(move)
    score = minimax(game, 5, False)
    game.board[move] = ' '
    print("Move:", move, "Score:", score)
    if score > best_score:
        best_score = score
        best_move = move
print("Best move:", best_move)
minimax_end = time.time()
print("time taken: " +str(minimax_end-minimax_start))

# Alpha-Beta Pruning
print("\nUsing Alpha-Beta Pruning:")
pruning_start = time.time()
best_move = None
best_score = -math.inf
for move in game.available_moves():
    game.make_move(move)
    score = alpha_beta_pruning(game, 5, -math.inf, math.inf, False)
    game.board[move] = ' '
    print("Move:", move, "Score:", score)
    if score > best_score:
        best_score = score
        best_move = move
print("Best move:", best_move)
pruning_end = time.time()
print("time taken: " +str(pruning_end-pruning_start))



speedup = (minimax_end-minimax_start)/(pruning_end-pruning_start)
print("The alpha beta pruning is faster than the normal MINIMAX by " + str(speedup) + " times")