import functools
class Solution:
    def __init__(self,board):
        self.board = board
        self.answer = [0,0,0,0] # left top right bottom
        self.numRookCaptures()
    def numRookCaptures(self) -> int:
        board = self.board
        for row,line in enumerate(board):
            for column,chesse in enumerate(line):
                if chesse == "R":
                    rookPosition = row,column

        row = rookPosition[0]
        column = rookPosition[1]
        # check left
        while column >= 0:
            if board[row][column]=="B":
                break
            elif board[row][column]=="p":
                self.answer[0]=1
                break
            column-=1

        column = rookPosition[1]
        # check right
        while column < len(board[row]):
            if board[row][column]=="B":
                break
            elif board[row][column]=="p":
                self.answer[2]=1
                break
            column+=1

        row = rookPosition[0]
        column = rookPosition[1]
        # check top
        while row >= 0:
            if board[row][column]=="B":
                break
            elif board[row][column]=="p":
                self.answer[1]=1
                break
            row-=1

        row = rookPosition[0]
        # check bottom
        while row < len(board):
            if board[row][column]=="B":
                break
            elif board[row][column]=="p":
                self.answer[3]=1
                break
            row+=1
        print(self.answer)
        num = functools.reduce(lambda a,b:a+b,self.answer)
        return num

if __name__=='__main__':
    board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
    s = Solution(board)
