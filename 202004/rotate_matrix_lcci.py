'''
示例 1:

给定 matrix = [ [1,2,3], [4,5,6], [7,8,9] ],

原地旋转输入矩阵，使其变为:
[ [7,4,1], [8,5,2], [9,6,3] ]
示例 2:

给定 matrix = [ [ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16] ], 

原地旋转输入矩阵，使其变为:
[ [15,13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7,10,11] ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-matrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(math.floor(size/2)):
            for j in range(i,size-i-1):
                matrix[i][j],matrix[j][size-i-1],matrix[size-i-1][size-j-1],matrix[size-j-1][i] = matrix[size-j-1][i],matrix[i][j],matrix[j][size-i-1],matrix[size-i-1][size-j-1]
        return matrix