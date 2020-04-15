from typing import List
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def refresh():
            vector_x = [1,-1,0,0]
            vector_y = [0,0,1,-1]
            # for v in range(4):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != 1:
                        for v in range(4):
                            if 0 <= vector_y[v]+i < len(matrix) and 0 <= vector_x[v]+j < len(matrix):
                                if matrix[vector_y[v]+i][vector_x[v]+j]==1:
                                    matrix[vector_y[v]+i][vector_x[v]+j] = -(abs(matrix[i][j])+1)
                                elif abs(matrix[vector_y[v]+i][vector_x[v]+j])>abs(matrix[i][j])+1:
                                    matrix[vector_y[v]+i][vector_x[v]+j] = -(abs(matrix[i][j])+1)
        while True:
            tmp = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
            refresh()
            if tmp == matrix:
                break
        return list(map(lambda row:list(map(lambda e: e,row)),matrix))
                    

if __name__ == "__main__":
    matrix = [
        [0,0,1,0,0],
        [0,1,1,1,0],
        [1,1,1,1,1]
    ]
    matrix = [
        [1,1,0,0,1,0,0,1,1,0],
        [1,0,0,1,0,1,1,1,1,1],
        [1,1,1,0,0,1,1,1,1,0],
        [0,1,1,1,0,1,1,1,1,1],
        [0,0,1,1,1,1,1,1,1,0],
        [1,1,1,1,1,1,0,1,1,1],
        [0,1,1,1,1,1,1,0,0,1],
        [1,1,1,1,1,0,0,1,1,1],
        [0,1,0,1,1,0,1,1,1,1],
        [1,1,1,0,1,0,1,1,1,1]
    ]
    # matrix = [[0] for _ in range(5)]
    s = Solution()
    m = s.updateMatrix(matrix)
    print(m)

