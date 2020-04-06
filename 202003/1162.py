from typing import List
import copy
class Solution:
    def __init__(self,grid: List[List[int]]):
        self.maxDistance(grid)
    def maxDistance(self, grid: List[List[int]]) -> int:
        step = 0
        new_grid = copy.deepcopy(grid)
        flag_val = grid[0][0]
        flag = True
        while True:
            step += 1
            direction_x = [0,1,0,-1]
            direction_y = [1,0,-1,0]
            for y,row in enumerate(grid):
                for x,column in enumerate(row):
                    if flag and column != flag_val:
                        flag = False
                    # island
                    if column == step :
                        for i in range(4):
                            if direction_x[i]+x >= 0 and direction_x[i]+x < len(grid) and direction_y[i]+y>=0 and direction_y[i]+y < len(grid) :
                                if grid[direction_y[i]+y][direction_x[i]+x] == 0:
                                    new_grid[direction_y[i]+y][direction_x[i]+x] = step+1
            # print('grid',grid)
            # print('new_grid',new_grid)
            if grid == new_grid:
                break
            grid = copy.deepcopy(new_grid)
        # print(step-1)
        # print(-1 if flag else step-1)
        return -1 if flag else step-1

if __name__ == '__main__':
    grid = [[0,0,0],[0,0,0],[0,0,0]]

    s = Solution(grid)