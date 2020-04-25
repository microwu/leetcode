from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo,hi = 0,len(height)-1
        res = min(height[lo],height[hi])*(hi-lo)
        while lo<hi:
            if height[hi]>height[lo]:
                lo+=1
            else:
                hi-=1
            if min(height[lo],height[hi])*(hi-lo) > res:
                res = min(height[lo],height[hi])*(hi-lo)
        return res


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    height = [1,2,4,3]
    height = [8,10,14,0,13,10,9,9,11,11]
    s = Solution()
    print(s.maxArea(height))

