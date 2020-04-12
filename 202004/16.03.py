# 16.03 intersection lcci
'''
给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。

要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。
示例 1：

输入：
line1 = {0, 0}, {1, 0}
line2 = {1, 1}, {0, -1}
输出： {0.5, 0}
示例 2：

输入：
line1 = {0, 0}, {3, 3}
line2 = {1, 1}, {2, 2}
输出： {1, 1}
示例 3：

输入：
line1 = {0, 0}, {1, 1}
line2 = {1, 0}, {2, 1}
输出： {}，两条线段没有交点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-lcci
'''
from typing import List
class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        # print(start1,end1,start2,end2)
        def y1(x):
            return a1*x+b1
        def y2(x):
            return a2*x+b2
        if start1[0] > end1[0]:
            start1,end1 = end1,start1
        if start2[0] > end2[0]:
            start2,end2 = end2,start2
        if start1[0] != end1[0]:
            a1 = (start1[1] - end1[1])/(start1[0]-end1[0])
            b1 = start1[1] - start1[0]*a1
        if start2[0] != end2[0]:
            a2 = (start2[1] - end2[1])/(start2[0]-end2[0])
            b2 = start2[1] - start2[0]*a2
        if start1[0] == end1[0]:
            if start2[0] == end2[0]:
                if start1[0]!=start2[0]:
                    return []
                if start1[1] > end1[1]:
                    start1,end1 = end1,start1
                if start2[1] > end2[1]:
                    start2,end2 = end2,start2
                if start1[1] > end2[1] or start2[1] > end1[1]:
                    return []
                elif start1[1] < end2[1] and end1[1] >= start2[1]:
                    return start2
                elif start2[1] < end1[1] and end2[1] >= start1[1]:
                    return start1
                return []
            return [start1[0],y2(start1[0])]
        if start2[0] == end2[0]:
            return [start2[0],y1(start2[0])]
        if a1 == a2 and b1 != b2 :
            return []
        elif b1==b2 :
            if start1[0] > end2[0] or start2[0] > end1[0]:
                return []
            elif start1[0] <= end2[0] and end1[0] >= start2[0]:
                return start2
            elif start2[0] <= end1[0] and end2[0] >= start1[0]:
                return start1
        x = (b2-b1)/(a1-a2)
        y = y1(x)
        if start1[0] <= x <= end1[0] and start2[0] <= x <= end2[0]:
            return [x,y]
        else:
            return []

if __name__ == "__main__":
    s = Solution()
    print(s.intersection([0,0],[1,0],[1,1],[0,-1]))
    print(s.intersection([0,0],[3,3],[1,1],[2,2]))
    print(s.intersection([0,0],[0,1],[0,0],[0,-1]))
    print(s.intersection([0,0],[1,1],[1,1],[3,3]))
    print(s.intersection([0,0],[1,1],[0,1],[99,0]))
    print(s.intersection([-10,48],[-43,46],[-16,59],[-1,85]))