import time
from player import HumanPlayer, ComputerPlayer_Random, ComputerPlayer_Genius

# The player ComputerPlayer_Genius would never let you win.
# But if you want to win with computer, change the player_o to ComputerPlayer_Random('O') in 
# (if __name__ == '__main__':). The same note is provided there.

class game_TicTacToe:
    def __init__(self):
        self.game_board = [' ' for _ in range(9)] #Created board
        self.current_winner = None #Winner

    def print_game_board(self):
        for board_row in [self.game_board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(board_row) + ' |')

    @staticmethod
    def print_board_nos():
        numbers_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] 
        for board_row in numbers_board:
            print('| ' + ' | '.join(board_row) + ' |')

    def moves_available(self):
        return[i for i, spot in enumerate(self.game_board) if spot == ' ']

    def squares_empty(self):
        return ' ' in self.game_board

    def num_squares_empty(self):
        return self.game_board.count(' ')

    def make_move(self, square, Letter_XO):
        if self.game_board[square] == ' ':
            self.game_board[square] = Letter_XO
            if self.winner(square, Letter_XO):
                self.current_winner = Letter_XO 
            return True
        return False

    def winner(self, square, Letter_XO):
        row_index = square//3 # check rows
        board_row = self.game_board[row_index*3 :(row_index + 1) * 3]
        if all([spot == Letter_XO for spot in board_row]):
            return True

        column_index = square % 3 # check columns
        column = [self.game_board[column_index+i*3] for i in range(3)]
        if all([spot == Letter_XO for spot in column]):
            return True

        if square % 2 == 0:# check diagonals
            diagonal_1 = [self.game_board[i] for i in [0, 4, 8]]
            if all([spot == Letter_XO for spot in diagonal_1]):
                return True

            diagonal_2 = [self.game_board[i] for i in [2, 4, 6]]
            if all([spot == Letter_XO for spot in diagonal_2]):
                return True

        return False #if all checks fail

def play(game, player_x, player_o, print_game = True):
    if print_game:
        game.print_board_nos()

    Letter_XO = 'X' #starting Letter_XO is X

    while game.squares_empty():
        if Letter_XO == 'O':
            square = player_o.get_move(game)
        else:
            square = player_x.get_move(game)

        if game.make_move(square, Letter_XO):
            if print_game:
                print(Letter_XO + f' makes a move to square {square}')
                game.print_game_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(Letter_XO + ' Wins!!!')
                return Letter_XO 

            Letter_XO = 'O' if Letter_XO == 'X' else 'X'
        
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    player_x = HumanPlayer('X')
    player_o = ComputerPlayer_Genius('O')  
    #The player ComputerPlayer_Genius would never let you win
    #But if you want to win with computer, change the player_o to ComputerPlayer_Random('O')
    G = game_TicTacToe()
    play(G, player_x, player_o, print_game = True)
