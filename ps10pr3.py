#
# ps10pr3.py  (Problem Set 10, Problem 3)
#
# Playing the game    
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(player, board):
    """ takes two parameters: a Player object for the player whose move is
        being processed, and a Board object for the game that is being played.

        The function will perform all of the steps involved in processing a
        single move by the specified player on the specified board.
    """
    count = 0
    player_turn = player.__repr__()
    print(player)
    player_move = player.next_move(board)
    if player_turn == 'Player X':
        count += 1
        add_check = board.add_checker('X', player_move)
        print()
        print(board)
        win = board.is_win_for('X')
        print()
        if win == True:
            print('Player X wins in', count, 'moves')
            print('Congratulations!')
            return True
        else:
            if board.is_full() != True:
                return False
            else:
                print('It''s a tie!')
                return True
    if player_turn == 'Player O':
        count += 1
        add_check = board.add_checker('O', player_move)
        print()
        print(board)
        win = board.is_win_for('O')
        print()
        if win == True:
            print('Player O wins in', count, 'moves')
            print('Congratulations!')
            return True
        else:
            if board.is_full() != True:
                return False
            else:
                print('It''s a tie!')
                return True

class RandomPlayer(Player):    
    """ RandomPlayer inherits from Player
    """
    def next_move(self, board):
        """ Overrides (i.e., replaces) the next_move method that is inherited
            from Player. Rather than asking the user for the next move, this
            version of next_move will choose at random from the columns in
            the specified board that are not yet full, and return the index
            of that randomly selected column.
        """
        self.num_moves += 0
        avail_col = []


        for col in range(board.width):
            function = board.can_add_to(col)
            if function == True:
                avail_col = avail_col + [col]
                self.num_moves += 0

        return random.choice(avail_col)
    
    
            
        
        
        
