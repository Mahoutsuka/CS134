# Lab 9 : Boggle

Collaboration: *enter names of others you worked with*

This repository contains the following files:
 - `README.md`: this file
 - `board.py`: implementation of a graphical board (base class)
 - `boggleboard.py`: boggle-specific extension of the Board base class
 - `bogglecube.py`: implementation of a single boggle cube
 - `bogglegame.py`: implementation of Boggle game logic
 - `bogwords.txt`: list of valid words
 - `brandom.py`: helper functions for implementing randomization features
 - `graphics.py`: code for the graphics library


## Assignment Expectations

Note that this lab counts as a double lab (worth the grade of two labs).
The expectations will be evaluated at the end of the second week.

### Functionality Requirements

 - Task 1:  `BoggleCube`
   * passes all instructor tests
   * implements all required methods
   * provides appropriate comments on logic of non-obvious code
   * uses good style with getters, setters
   * uses helper methods when appropriate

 - Task 2: `BoggleBoard`
   * passes all instructor tests
   * implements all required methods
   * provides appropriate comments on logic of hard-to-read code
   * uses good style with getters, setters
   * uses helper methods when appropriate
   * correctly implements shake_cubes to produce valid game board (no repeated cubes)
   * correctly implements `is_adjacent`
   * utilizes methods from inherited class to avoid code duplication

 - Task 3: `BoggleGame`
   * correctly implements game logic
   * grid colors change appropriately as words are formed
   * words-in-progress appear in lower text area
   * completed valid words appear in right text area
   * correctly handles reset and exit
   * provides appropriate comments on logic of hard-to-read code
   * uses methods from other classes appropriately
   * uses consistent style throughout
   * uses helper methods to reduce redundant code


## Style and Global Requirements

   * Does not use language features that were not discussed in class
   * Code makes good use of variable names, and is clear and readable
   * 1-3 appropriate comments per function, explaining complex logic
   * Adds helper methods when appropriate
