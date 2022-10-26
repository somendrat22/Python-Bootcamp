class MainImpl:

    def __init__(self, Board, player1, player2):
        self.Board = Board
        self.board = Board.board
        self.rowCount = Board.rowCount
        self.colCount = Board.colCount
        self.dig = Board.dig
        self.antiDig = Board.antiDig
        
    

    def putCrossOrZero(self, row, col, ch):
        if self.board[row][col] != '_':
            print("Hii you choose wrong position... please choose accordingly")
            return -1 # -1 represent some -ve happen please correct it 
        self.board[row][col] = ch
        if ch == 'X':
            self.rowCount[row] -= 1
            self.colCount[col] -= 1
            if row == col:
                self.dig -= 1
            if row + col == 2:
                self.antiDig -= 1
        else:
            self.rowCount[row] += 1
            self.colCount[col] += 1
            if row == col:
                self.dig += 1
            if row + col == 2:
                self.antiDig += 1
        if(self.colCount[col] ==  3 or self.rowCount[row] == 3 or self.antiDig == 3 or self.dig == 3 or self.rowCount[row] == -3 or self.colCount[col] == -3 or self.dig == -3 or self.antiDig == -3):
            return 2  # We will return 2 when some one won the game
        return 1 # when no body won we will return q which will represent game is still on 

        






