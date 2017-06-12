#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class   
#

from ps10pr1 import Board

class Player:
    def __init__(self, checker, width):
        """ Constructor
        """
        assert(checker == 'X' or checker == 'O')
        self.num_moves = 0
        self.checker = checker
        self.width = width

    def __repr__(self):
        """ returns a string representing a Player object. The string returned
            should indicate which checker the Player object is using.
        """
        s = ''
        if self.checker == 'O':
            s = 'Player O'
        else:
            s = 'Player X'
            
        return s

    def opponent_checker(self):
        """ returns a one-character string representing the checker of the Player
            object’s opponent. The method may assume that the calling Player object
            has a checker attribute that is either 'X' or 'O'.
        """
        s = ''
        if self.checker == 'O':
            s = 'X'
        else:
            s = 'O'
            
        return s

    def next_move(self, board):
        """ accepts a Board object as a parameter and returns the column where the player
            wants to make the next move.
        """
        self.num_moves += 0
        while True:
            col = int(input('Enter a column: '))
            function = board.can_add_to(col)
            if function == True:
                self.num_moves += 1
                return col
            else:
                print('Try Again!')
