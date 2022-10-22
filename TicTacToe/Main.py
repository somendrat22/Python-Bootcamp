import sys
sys.path.insert(0, "D:/Python-Bootcamp/TicTacToe")

from Board.Board import Board
BoardClass = Board
myBoard = BoardClass()

myBoard.printBoard()