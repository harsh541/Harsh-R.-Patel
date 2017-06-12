#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps10pr3 import *

class AIPlayer(Player):
    """ AIPlayer inherits from Player
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ Constructor
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        super().__init__(checker, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ Returns a string representing an AIPlayer object. This method will
            override/replace the __repr__ method that is inherited from Player.
            In addition to indicating which checker the AIPlayer object is using,
            the returned string will also indicate the player’s tiebreaking strategy
            and lookahead.
        """
        s = ''
        if self.checker == 'O':
            s = 'Player O '
        else:
            s = 'Player X '

        if self.tiebreak == 'LEFT':
            s += "(LEFT, "
        if self.tiebreak == 'RIGHT':
            s += "(RIGHT, "
        if self.tiebreak == 'RANDOM':
            s += "(RANDOM, "
        look = self.lookahead
        s += str(look)
        s += ')'
        return s

    def max_score_column(self, scores):
        """ Takes a list scores containing a score for each column of the board,
            and that returns the index of the column with the maximum score. If one
            or more columns are tied for the maximum score, the method should apply
            the called AIPlayer‘s tiebreaking strategy to break the tie.
        """
        num = max(scores)
        index = []


        for x in range(len(scores)):
            if num == scores[x]:
                index += [x]
        if self.tiebreak == 'LEFT':
            return index[0]
        if self.tiebreak == 'RIGHT':
            return index[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(index)

    def scores_for(self, board):
        """ Takes a Board object board and determines the called AIPlayer‘s scores for
            the columns in board. Each column will be assigned one of the four possible
            scores discussed in the Overview at the start of this problem, based on the
            called AIPlayer‘s lookahead value. The method will return a list containing
            one score for each column.
        """
        scores = [50] * board.width
        opponentchecker = ''
        if self.checker == 'O':
            opponentchecker += 'X'
        else:
            opponentchecker += 'O'

        for col in range(board.width):
            can_add = board.can_add_to(col)
            if can_add == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                oppo_scores = opponent.scores_for(board)
                scores[col] = 100 - max(oppo_scores)
                board.remove_checker(col)
                
        return scores

    def next_move(self, board):
        """ Overrides (i.e., replaces) the next_move method that is inherited from Player. Rather
            than asking the user for the next move, this version of next_move will return the
            called AIPlayer‘s judgment of its best possible move.
        """
        self.num_moves += 0

        #for col in range(board.width):
        scores = AIPlayer.scores_for(self, board)
        max_m = AIPlayer.max_score_column(self, scores)
        self.num_moves += 1
        return max_m
