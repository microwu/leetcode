from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals,key = lambda e:e[0])
        res = [intervals[0]]
        for i in range(len(intervals)):
            if intervals[i][0] <= res[-1][1] and intervals[i][1] > res[-1][1]:
                res[-1] = [res[-1][0],intervals[i][1]]
            elif intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
        return res

if __name__ == "__main__":
    intervals = [[2,6],[1,3],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]
    s = Solution()
    res = s.merge(intervals)
    print(res)