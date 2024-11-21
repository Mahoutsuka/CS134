"""Implements the logic of the game of boggle."""

from graphics import GraphWin
from boggleboard import BoggleBoard
from bogglecube import BoggleCube
from brandom import randomize

class BoggleGame:  
    # Description of attributes:
    # _valid_words: the set of all valid Boggle words
    # _board: the BoggleBoard
    # _found_words: a list of strings of all words found so far
    # _selected_cubes: a list of BoggleCubes selected in current turn

    __slots__ = [ "_valid_words", "_board", "_found_words", "_selected_cubes" ]

    def __init__(self, win):
        """
        Create a new Boggle Game and load in our lexicon.
        """
        # set up the set of valid words we can match
        self._valid_words = self.__read_lexicon()

        # initialize and draw a BoggleBoard
        self._board = BoggleBoard(win)
        self._board.draw_board()

        self._found_words = []
        self._selected_cubes = []
        pass # replace this line with your code

    def __read_lexicon(self, lexicon_name='bogwords.txt'):
        """
        A helper method to read the lexicon and return it as a set.
        """
        # DO NOT MODIFY.
        valid_words = set()
        with open(lexicon_name) as f:
          for line in f:
            valid_words.add(line.strip().upper())

        return valid_words

    def __reset_game(self):
        """
        Updates all game state to reflect the start of a "new" game
        """

        #Randomize letter in Boggle Box
        self._board.shake_cubes()
        self._board.reset()
        self._selected_cubes = []
        self._found_words = []

    def __reset_turn(self):
        """
        Reset current turn by resetting state of selected cubes 
        as well as resetting any associated grid graphics (highlighted 
        letters or colored cells) and text from current word displayed on board
        """
        for cube in self._selected_cubes:
            coords = self._board.get_bogglecube_coords(cube)
            self._board.set_grid_cell(coords[0],coords[1],cube)
        self._selected_cubes = []
        self._board.set_string_to_lower_text("")

    def __highlight_cube(self, cube, text_color, fill_color):
        """
        Highlights a given cube by setting background grid cell to fill_color
        and text in cell to text_color.
        """
        # DO NOT MODIFY.
        r, c = self._board.get_bogglecube_coords(cube)
        letter = cube.get_letter()
        self._board.set_grid_cell(r, c, letter, text_color, fill_color)

    def __add_cube_to_word(self, cube):
        """
        Extends the current word (displayed on lower text area) by
        adding the visible letter from given cube
        """
        new_lower_text = self._board.get_string_from_lower_text() + cube.get_letter()
        self._board.set_string_to_lower_text(new_lower_text)
        

    def __selected_cubes_to_word(self):
        """
        Returns the word spelled by the visible face of all selected cubes
        """
        word = ""
        for cube in self._selected_cubes:
            word = word + cube.get_letter()
        return word
    
    def all_found_words (self, word):
        new_text = self._board.get_string_from_text_area + "\n" + word
        self._board.set_string_to_text_area(new_text)

    def do_one_click(self, point):
        """
        Implements the logic for processing one click.
        Returns True if play should continue, and False if the game is over.
        """
        if self._board.in_grid(point):
            cube_clicked = self._board.get_bogglecube_at_point(point)
            if self._selected_cubes == []:
                self.__highlight_cube(cube_clicked, "blue", "powder blue")
                self.__add_cube_to_word(cube_clicked)
                self._selected_cubes += [cube_clicked]
            else: 
                prev_cube = self._selected_cubes[len(self._selected_cubes)-1]
                if prev_cube == cube_clicked: 
                    word = self.__selected_cubes_to_word()
                    if word in self._valid_words:
                        self._found_words += [word]
                        self.all_found_words(word)
                    self.__reset_turn()
                elif cube_clicked in self._selected_cubes or not self._board.is_adjacent(cube_clicked,prev_cube):
                    self.__reset_turn()
                elif self._board.is_adjacent(cube_clicked, prev_cube):
                    self.__highlight_cube(prev_cube, "DarkSeaGreen1", "green")
                    self.__highlight_cube(cube_clicked, "blue", "powder blue")
                    self.__add_cube_to_word(cube_clicked)
                    self._selected_cubes += [cube_clicked]
        else:


    
            
            
                
           
           
           
       
           

            if prev_cube == cube_clicked:
        # see handout for a step-by-step guide on how to implement this method
        if self._board.in_exit(point):
            return False
        if self._board.in_reset(point):
            self._board.reset
            self._board.shake_cubes
        cube_clicked = self._board.get_bogglecube_at_point(point)
        if self._selected_cubes[len(self._selected_cubes)-1] == cube_clicked:
            return 
    
        return True

if __name__ == '__main__':

    # When you are ready to run on different boards,
    # insert a call to randomize() here.  BUT you will
    # find it much easier to test your code without
    # randomizing things!

    win = GraphWin("Boggle", 400, 400)
    game = BoggleGame(win)
    keep_going = True
    while keep_going:
        point = win.getMouse()
        keep_going = game.do_one_click(point)
