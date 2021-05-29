import numpy as np
import datetime

class SudokuSolver:

    def __init__(self, start_board):
        self.final_board = np.array([])
        self.start_board = start_board

    def solve(self, newBoard):
        newBoard.shape = 9,9
        position = self.return_empty_position(newBoard)
        if not position:
            return True
        else:
            row, col = position

        for i in range(1, 10):
            newBoard.shape = 9,9
            num_index = row * 9 + col
            if(self.valid(newBoard, num_index,str(i))):
                newBoard[row][col] = str(i)

                if(self.solve(newBoard)):
                    return True
                newBoard.shape = 9,9
                newBoard[row][col] = "0"
        return False


    def valid(self, board, index, number):
        if(self.fitsInBlock(board, index, number) and self.fitsVertically(board, index, number) and self.fitsHorizontally(board, index, number)):
            return True
        else:
            return False

    def fitsInBlock(self, board, index, number):
        rowIndex = self.currentRow(index)
        board.shape = 9,9
        columnIndex = self.getIndexInRow(board, index)
        if(rowIndex <= 2):
            if(columnIndex <=-7):
                block = self.buildBlock(board, 1, 1)
                if number in block:
                    return False
               
                return True
            elif(columnIndex <= -4):
                block = self.buildBlock(board, 1, 2)
                if number in block:
                    return False
               
                return True
            elif(columnIndex <= -1):
                block = self.buildBlock(board, 1, 3)
                if number in block:
                    return False
               
                return True
            else:
                pass
        elif(rowIndex <= 5):
            if(columnIndex <=-7):
                block = self.buildBlock(board, 2, 1)
                if number in block:
                    return False
               
                return True
            elif(columnIndex <= -4):
                block = self.buildBlock(board, 2, 2)
                if number in block:
                    return False
               
                return True
            elif(columnIndex <= -1):
                block = self.buildBlock(board, 2, 3)
                if number in block:
                    return False
               
                return True
            else:
                pass
        elif(rowIndex <= 8):
            if(columnIndex <=-7):
                block = self.buildBlock(board, 3, 1)
                if number in block:
                    return False
               
                return True
            elif(columnIndex <= -4):
                block = self.buildBlock(board, 3, 2)
                if number in block:
                    return False
               
                return True
            elif(columnIndex <= -1):
                block = self.buildBlock(board, 3, 3)
                if number in block:
                    return False
               
                return True
            else:
                pass

        else:
            pass

        return False


    def fitsVertically(self, board, index, number):
        board.shape = 9,9
        columnBoard = self.convertToColumn(board, index)
        if(number in columnBoard):
            return False
        return True

    def fitsHorizontally(self, board, index, number):
        board.shape = 9, 9
        if number in board[self.currentRow(index)]:
            return False
        return True

    def return_empty_position(self, board):
        board.shape = 9,9
        for i in range(len(board)):
            for n in range(len(board[0])):
                if(board[i][n] == "0"):
                    return (i, n)
        return None

    def currentRow(self, index):
        value = index/9
        if(value < 1):
            return 0
        elif(value < 2):
            return 1
        elif(value < 3):
            return 2
        elif(value < 4):
            return 3
        elif(value < 5):
            return 4
        elif(value < 6):
            return 5
        elif(value < 7):
            return 6
        elif(value < 8):
            return 7
        elif(value < 9):
            return 8
        return null

    def getIndexInRow(self, board,index):
        board.shape = 9,9
        rowIndex = self.currentRow(index)
        actualRow = rowIndex + 1
        columnIndex = index - actualRow*9
        return columnIndex

    def convertToColumn (self, board, index):
        board.shape = 9,9
        columnIndex = self.getIndexInRow(board, index)
        column = np.array([])
        for x in board:
            column = np.append(column, x[columnIndex])
        return column

    def buildBlock(self, board, y, x):
        board.shape = 9,3,3

        block = np.array([])
        if(y == 1 and x == 1):
            for i in range(3):
                block = np.append(block, board[i][0])
        elif(y == 1 and x == 2):
            for i in range(3):
                block = np.append(block, board[i][1])
        elif(y == 1 and x == 3):
            for i in range(3):
                block = np.append(block, board[i][2])
        elif(y == 2 and x == 1):
            for i in range(3, 6, 1):
                block = np.append(block, board[i][0])
        elif(y == 2 and x == 2):
            for i in range(3, 6, 1):
                block = np.append(block, board[i][1])
        elif(y == 2 and x == 3):
            for i in range(3, 6, 1):
                block = np.append(block, board[i][2])
        elif(y == 3 and x == 1):
            for i in range(6, 9, 1):
                block = np.append(block, board[i][0])
        elif(y == 3 and x == 2):
            for i in range(6, 9, 1):
                block = np.append(block, board[i][1])
        elif(y == 3 and x == 6, 9, 1):
            for i in range(6, 9, 1):
                block = np.append(block, board[i][2])


    
        return block


    def main(self):
        self.solve(self.start_board)
        return self.start_board

def print_formated_board(board):
    board.shape = 9,9
    for x in range(9):
        if x % 3 == 0 and x != 0:
            print("************************")

        for i in range(9):
            if i % 3 == 0 and i != 0:
                print(" | ", end="")

            if i == 8:
                print(board[x][i])
            else:
                print(str(board[x][i]) + " ", end="")

board = np.array([
    ["6", "0", "0", "0", "0", "0", "5", "3", "0" ],
    ["0", "0", "0", "0", "0", "2", "7", "0", "0" ],
    ["5", "0", "7", "0", "9", "6", "0", "1", "8" ],
    ["0", "0", "6", "0", "0", "1", "0", "8", "0" ],
    ["0", "9", "8", "0", "0", "0", "0", "0", "0" ],
    ["0", "0", "0", "0", "2", "0", "0", "0", "0" ],
    ["0", "0", "0", "0", "0", "0", "9", "0", "0" ],
    ["0", "0", "0", "2", "0", "0", "0", "4", "3" ],
    ["3", "1", "0", "0", "0", "9", "0", "6", "2" ]
])

if __name__ == "__main__":
    print("\n\nStart board:\n")
    print_formated_board(board)
    solver = SudokuSolver(board)
    a = datetime.datetime.now()
    solved_board = solver.main()
    b = datetime.datetime.now()
    print("\n\nFinal board:\n")
    print_formated_board(solved_board)
    print("\n", b-a)


