"""
Extends the Board class with specific features required for Boggle
"""

from graphics import *
from brandom import *
from bogglecube import BoggleCube
from board import Board

# CUBE_FACES stores a list of tuples that represent the unique legal faces
# for BoggleCube objects
CUBE_FACES = [("A", "A", "C", "I", "O", "T"),  # cube 0 
              ("T", "Y", "A", "B", "I", "L"),  # cube 1
              ("J", "M", "O", "QU", "A", "B"), # cube 2
              ("A", "C", "D", "E", "M", "P"),  # cube 3
              ("A", "C", "E", "L", "S", "R"),  # cube 4
              ("A", "D", "E", "N", "V", "Z"),  # cube 5
              ("A", "H", "M", "O", "R", "S"),  # cube 6
              ("B", "F", "I", "O", "R", "X"),  # cube 7
              ("D", "E", "N", "O", "S", "W"),  # cube 8
              ("D", "K", "N", "O", "T", "U"),  # cube 9
              ("E", "E", "F", "H", "I", "Y"),  # cube 10
              ("E", "G", "I", "N", "T", "V"),  # cube 11
              ("E", "G", "K", "L", "U", "Y"),  # cube 12
              ("E", "H", "I", "N", "P", "S"),  # cube 13
              ("E", "L", "P", "S", "T", "U"),  # cube 14
              ("G", "I", "L", "R", "U", "W")]  # cube 15


class BoggleBoard(Board):
    """
    BoggleBoard class implements the functionality of a Boggle board.
    It inherits from the Board class and extends it by creating a list
    of BoggleCubes, which can be shaken to randomize play.
    Each BoggleCube corresponds to a specific (row, col) grid cell
    on the board.
    """

    # _cubes: a list of BoggleCube objects
    
    __slots__ = [ "_cubes" ]

    def __init__(self, win):
        super().__init__(win, rows=4, cols=4)

        # Board is initially empty
        self._cubes = []
        for i in range(len(CUBE_FACES)):
            boggle_cube = BoggleCube(CUBE_FACES[i])
            self._cubes.append(boggle_cube)
            self.set_grid_cell(self._which_row(i), self._which_col(i), boggle_cube)
        print (self._cubes)

        self.place_cubes_on_board()


    def _which_row(self, cube_number) :
        """
        The row of the board's grid that corresponds to the
        BoggleCube at index cube_number
        """
        return cube_number // self._cols

    def _which_col(self, cube_number) :
        """
        The column of the board's grid that corresponds
        to the BoggleCube at index cube_number
        """
        return cube_number % self._cols

    def _which_cube(self, row, col) :
        """
        The index of the cube within the board's cube list that corresponds
        to the cube appearing at cell (row,col) of the board's grid
        """
        return (row * self._cols) + col
        
    def get_bogglecube_at_point(self, point):
        """
        Return the BoggleCube at the given point in the window,
        or None if the click is outside the letter grid.
        """
        if self.in_grid(point):
            index = self._which_cube(self.get_position(point)[0], self.get_position(point)[1])
            return self._cubes[index]
        return None

    def get_bogglecube_coords(self, bogglecube) :
        """
        Returns the a tuple of the (row, col) position that corresponds
        to a given BoggleCube's position in the grid
        """
        for i in range(len(self._cubes)):
            if self._cubes[i] == bogglecube:
                return (self._which_row(i), self._which_col(i))
                


    def reset(self):
        """
        Resets the letter/background colors of all cells on the
        grid back to their default values, and clears all text
        areas (right, lower, upper) on board.
        """
        # Reset colors
        self.reset_grid_graphics()

        # Reset text areas
        self.set_string_to_text_area("")
        self.set_string_to_lower_text("")
        self.set_string_to_upper_text("")


    
    def shake_cubes(self):
        """
        Randomizes the BoggleCube locations and randomizes the visible
        face for each BoggleCube.   
        """

        # Randomize which face is shown on the individual cube
        for cube in self._cubes:
            cube.randomize()

        # Shuffle the positions of the 16 cubes
        self._cubes = shuffled(self._cubes)
        
    def is_adjacent(self, cube1, cube2):
        """
        Given two BoggleCubes, cube1 and cube2, checks if the cubes'
        coordinates are adjacent.
        Returns True if they are adjacent, and False otherwise.
        Two coordinates are considered adjacent if they are not the same, and
        if their corresponding row and col coordinates differ by at most 1.
        """
        cube1_coords = self.get_bogglecube_coords(cube1)
        cube2_coords = self.get_bogglecube_coords(cube2)

        # Return true if the criteria (as outlined in the docstring) are met
        if cube1_coords != cube2_coords:
            if abs(cube1_coords[0] - cube2_coords[0]) <= 1 and abs(cube1_coords[1] - cube2_coords[1]) <= 1:
                return True
        return False

    def place_cubes_on_board(self):
        # DO NOT MODIFY  
        '''Updates the board to display the letters on BoggleCubes'''
        for i in range(len(self._cubes)):
            r = self._which_row(i)
            c = self._which_col(i)
            self._grid[r][c].setText(self._cubes[i].get_letter())


    def __str__(self):
        """
        Returns a string representation of this BoggleBoard.
        DO NOT MODIFY.
        """

        if len(self._cubes) == 0:
            return ''

        board = 'BoggleBoard:\n'
        for row in range(self._rows):
            board += str(row) + ": "
            for col in range(self._cols):
                cube = self._cubes[self._which_cube(row, col)]
                letter = cube.get_letter()
                board += '[{}] '.format(letter)
            board += '\n'
        return board


    
if __name__ == "__main__":
    pass
    # Uncomment this code when you are ready to test it!
    
    # # When you are ready to run on different boards,
    # # insert a call to randomize() here.  BUT you will
    # # find it much easier to test your code without
    # # randomizing things!

    

    win = GraphWin("Boggle", 400, 400)
    board = BoggleBoard(win)
    print(board)

    board.draw_board()


    keep_going = True
    while keep_going:
         pt = win.getMouse()
         if board.in_exit(pt):
             keep_going = False
         elif board.in_reset(pt):
             board.shake_cubes()
         elif board.in_grid(pt):
             # the grid coordinates where we clicked
             (x,y) = board.get_position(pt)

             # look up the cube that is stored at position (x,y)
             print("clicked coordinates ({}, {})...".format(x, y), end="")
             cube = board.get_bogglecube_at_point(pt)
             print(" and found cube {}".format(cube))

             # check that we can recover the correct coordinates
             # that the cube was stored at (a "reverse lookup")
             print("looking up cube {}...".format(cube), end="")
             (x, y) = board.get_bogglecube_coords(cube)
             print(" it is stored at pos ({}, {})".format(x, y))

