import math
import random

class AnyPlayer:
    def __init__(self, Letter_XO):
        self.Letter_XO = Letter_XO 

    def get_move(self, game):
        pass

class ComputerPlayer_Random(AnyPlayer):
    def __init__(self, Letter_XO):
        super().__init__(Letter_XO)

    def get_move(self, game):
        square = random.choice(game.moves_available())
        return square

class HumanPlayer(AnyPlayer):
    def __init__(self, Letter_XO):
        super().__init__(Letter_XO)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.Letter_XO + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.moves_available():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid square. Try again.')
        return val
        
class ComputerPlayer_Genius(AnyPlayer):
    def __init__(self, Letter_XO):
      super().__init__(Letter_XO)

    def get_move(self, game):
        if len(game.moves_available()) == 9:
            square = random.choice(game.moves_available())
        else:
            square = self.minimax(game, self.Letter_XO)['position']
        return square

    def minimax(self, state, player):
        playermax = self.Letter_XO
        playerother = 'O' if player == 'X' else 'X'

        if state.current_winner == playerother:
            return {'position': None,
                    'score': 1 *(state.num_squares_empty() + 1) if playerother == playermax 
                        else -1 * (state.num_squares_empty() + 1)
                    }

        elif not state.squares_empty():
            return {'position': None, 'score': 0}

        if player == playermax:
            best_move = {'position' : None, 'score': -math.inf}
        else:
            best_move = {'position' : None, 'score': math.inf}
        
        for move_possible in state.moves_available():
            state.make_move(move_possible, player)
            sim_score = self.minimax(state, playerother)

            state.game_board[move_possible] = ' '
            state.current_winner = None
            sim_score['position'] = move_possible

            if player == playermax:
                if sim_score['score'] > best_move['score']:
                    best_move = sim_score
            else:
                if sim_score['score'] < best_move['score']:
                    best_move = sim_score
                    
        return best_move
