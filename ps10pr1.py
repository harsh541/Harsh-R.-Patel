# Harsh Patel
#
# hrpatel@bu.edu
#
# ps10pr1.py

class Board:
    def __init__(self, height, width):
        """ Constructor
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string
        count = 0

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'
                

            s += '\n'  # newline at the end of the row

        for row in range(self.width):
            s += '--'
        s += '-'
        s += '\n'
        
        for row in range(self.width):  # newline at the end of the row
            count += 1
            real_c = count - 1
            if count == 10:
                count = 0
            s += ' ' + str(real_c)

        return s
    
    def add_checker(self, checker, col):
        """ That accepts two inputs:
            * Checker, a one-character string that specifies the checker to add to the board (either 'X' or 'O').
            * col, an integer that specifies the index of the column to which the
              checker should be added and that adds checker to the appropriate row in column col of the board.
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = 0
        while row < self.height and self.slots[row][col] == ' ':
            row += 1
        self.slots[row - 1][col] = checker

    def reset(self):
        """ Resets and board and clears all peices
        """
        row = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] != ' ':
                    self.slots[row][col] = ' '
                    
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the
            column col on the calling Board object. Otherwise, it should return False.
        """

        row = 0
        if -1 > col or col >= self.width:
            return False
        while row < self.height:
            if self.slots[row][col] == ' ':
                return True
            else:
                row += 1
        return False

    def is_full(self):
        """ returns True if the board is full, False otherwise.
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == ' ':
                    return False
        return True
    
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object.
            If the column is empty, then the method should do nothing.
        """
        row = 0
        if row < self.height:
            while row < self.height -1 and self.slots[row][col] == ' ':
                row += 1
            self.slots[row][col] = ' '

    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a virtical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a up diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False
    
    def is_win_for(self, checker):
        """ Accepts a parameter checker that is either 'X' or 'O', and returns True
            if there are four consecutive slots containing checker on the board. Otherwise,
            it should return False.
        """
        assert(checker == 'X' or checker == 'O')

        # call the helper functions and use their return values to
        # determine whether to return True or False
        
        vert = self.is_vertical_win(checker)
        horiz = self.is_horizontal_win(checker)
        up = self.is_up_diagonal_win(checker)
        down = self.is_down_diagonal_win(checker)
        if vert == True or horiz == True or up == True or down == True:
            return True
        else:
            return False
