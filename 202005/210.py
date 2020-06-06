from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        matrix = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for pair in prerequisites:
            matrix[pair[0]][pair[1]] = 1
        # print(matrix)
        res = []
        return res

if __name__ == "__main__":
    s = Solution()
    s.findOrder(4,[[1,0],[2,0],[3,1],[3,2]])