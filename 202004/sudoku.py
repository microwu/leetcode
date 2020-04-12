'''
空白格用 '.' 表示。
给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
'''
from typing import List
def print_board(board):
    print("|"+"-"*29+"|")
    for i,row in enumerate(board):
        print("|",end="")
        for j,column in enumerate(row):
            print("{:^3}".format(column),end="|" if (j+1)%3==0 else "")
        print("")
        if i%3 == 2:
            print("|"+"-"*29+"|")
        
class Solution:
    def __init__(self,board):
        self.pos_stack = []
        self.solveSudoku(board)
    def check(self,num,pos):
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1,10):
                        if self.check(num,pos) == True:




if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution(board)
    print_board(board)