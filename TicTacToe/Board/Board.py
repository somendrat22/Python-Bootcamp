
class Board:

    def __init__(self): 
        self.board = [['_','_','_'], ['_','_','_'],['_', '_', '_']]
        self.rowCount = [0, 0, 0]
        self.colCount = [0, 0, 0]
        self.dig = 0
        self.antiDig = 0
        
    def printBoard(self):
        length = len(self.board[0])

        for i in range(0, length):
            for j in range(0, length):
                print(self.board[i][j], end = "\t")
            print()    


