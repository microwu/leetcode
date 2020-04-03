'''
如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡； 
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活； 
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
if 1:
    if [0,1] :
        0
    elif [2,3]:
        1
    elif [4:8]:
        0
elif 0:
    if 3:
        1

[0,1,0],
[0,0,1],
[1,1,1],
[0,0,0]

[0,0,0],
[1,0,1],
[0,1,1],
[0,1,0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/game-of-life
'''
from typing import List
def print_board(board):
    p_str = ""
    for row in board:
        for cell in row:
            p_str += "{:^3}".format(cell)
        p_str += '\n'
    print(p_str)
class Solution:
    def __init__(self,board):
        self.gameOfLife(board)
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        print_board(board)
        vector_x = [1,1,1,0,0,-1,-1,-1]
        vector_y = [1,0,-1,1,-1,1,0,-1]
        for x,row in enumerate(board):
            for y,cell in enumerate(row):
                temp = 0
                for i in range(8):
                    if (x+vector_x[i] >= 0 
                    and y+vector_y[i] >= 0
                    and x+vector_x[i] < len(board) 
                    and y+vector_y[i] < len(row)
                    and board[x+vector_x[i]][y+vector_y[i]]>0): # used to be alive
                        temp+=1
                if cell > 0 :
                    board[x][y] = temp+1
                else :
                    board[x][y] = -temp
        print_board(board)
        for x,row in enumerate(board):
            for y,cell in enumerate(row):
                if cell > 0:
                    cell -= 1
                    if cell in [0,1] or cell >= 4:
                        board[x][y] = 0
                    else:
                        board[x][y] = 1
                if cell < 0:
                    if abs(cell) == 3:
                        board[x][y] = 1
                    else:
                        board[x][y] = 0
        self.board = board
    def __str__(self):
        p_str = ""
        for row in self.board:
            for cell in row:
                p_str += "{:^3}".format(cell)
            p_str += '\n'
        return p_str
                        
                        
        
if __name__ == "__main__":
    # s = Solution([
    #     [0,1,0],
    #     [0,0,1],
    #     [1,1,1],
    #     [0,0,0]
    # ])
    # print(s)
    # s = Solution([[0,0]])
    s = Solution([[1,0,0,0,0,1],[0,0,0,1,1,0],[1,0,1,0,1,0],[1,0,0,0,1,0],[1,1,1,1,0,1],[0,1,1,0,1,0],[1,0,1,0,1,1],[1,0,0,1,1,1],[1,1,0,0,0,0]])
    print(s)
    print_board([[0,0,0,0,1,0],[0,1,0,1,1,1],[0,1,0,0,1,1],[1,0,0,0,1,1],[1,0,0,0,0,1],[0,0,0,0,0,0],[1,0,1,0,0,0],[1,0,1,1,0,1],[1,1,0,0,1,0]])
