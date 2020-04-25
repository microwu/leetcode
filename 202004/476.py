from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit(i,j,grid):
            grid[i][j] = "-1"
            vector_x = [1,-1,0,0]
            vector_y = [0,0,1,-1]
            for k in range(4):
                if 0<=i+vector_y[k]<len(grid) and 0<=j+vector_x[k]<len(grid[0]) and grid[i+vector_y[k]][j+vector_x[k]]=="1":
                    visit(i+vector_y[k],j+vector_x[k],grid)
        res = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    visit(row,column,grid)
                    res += 1
        return res

if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"],
    ]
    s = Solution()
    print(s.numIslands(grid))