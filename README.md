You need to visualize the game 2048 in this project, which will be a 4 * 4
grid(matrix), initially there would be 2 random cells with a number 2 in it, the
rest are empty(try to think about how to represent empty cells), and for
each round, you generate a new random 2 for an empty cell. Users can
press w, s, a, d to move up, down, left, or right. When users press any key,
the elements of the cell move in that direction such that if any two numbers
are at the same row when you move horizontally, or in the same column
when you move vertically they get added up in that direction and fill itself
with that number, the rest cells go empty again. If no numbers are the same
and next to each other with one move, all numbers will move to the same
direction to fill all the space at that row/column. If you reach 2048, you win
the game, and can restart the game or end. If you cannot make further
moves, end the game or restart the game.

In this project, you need to use exception handling to handle all invalid
inputs. You need to include two files, the first file is the main file where you
run all the codes and will import all functions from the second file, and the
second python file contains all the functions you need
