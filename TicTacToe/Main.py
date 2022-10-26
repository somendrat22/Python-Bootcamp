from random import randint, random
import sys
sys.path.insert(0, "D:/Python-Bootcamp/TicTacToe")
from Board.Board import Board
from MainImpl.MainImpl import MainImpl


BoardClass = Board
myBoard = BoardClass()

player1 = input("Enter Name of Player1 : ")
player2 = input("Enter Name of Player2 : ")
toss = randint(0, 2)
player1Char = ""
player2Char = ""
firstPlayer = ""
firstPlayerChar = ""
secondPlayer = ""
secondPlayerChar = ""
if toss == 1:
    player1Char = input("{} please enter your charcater ".format(player1))
    player2Char = input("{} please enter your charcater ".format(player2))
    firstPlayer = player1
    secondPlayer = player2
    firstPlayerChar = player1Char
    secondPlayerChar = player2Char
else:
    player2Char = input("{} please enter your charcater ".format(player2))
    player1Char = input("{} please enter your charcater ".format(player1))
    firstPlayer = player2
    secondPlayer = player1
    firstPlayerChar = player2Char
    secondPlayerChar = player1Char
MainImpl = MainImpl(myBoard, firstPlayer, secondPlayer)
count = 0
while(count < 9):
    currPlayer = ""
    currCharacter = ""
    if count%2 == 0:
        currPlayer = firstPlayer
        currCharacter = firstPlayerChar
    else:
        currPlayer = secondPlayer
        currCharacter = secondPlayerChar
    myBoard.printBoard()
    row = int(input("{} please enter the row :".format(currPlayer)))
    col = int(input("{} please enter the col :".format(currPlayer)))
    res = MainImpl.putCrossOrZero(row,col, currCharacter)
    if res == 2:
        print("Congratulations {} you won the game !!".format(currPlayer))
        break
    elif res == -1:
        print("Wrong Move")
    else:
        count += 1

myBoard.printBoard()
