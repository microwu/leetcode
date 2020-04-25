'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
'''
from typing import List
import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def per(temp,unused):
            if not len(unused):
                res.append(temp)
                return
            unused_ = copy.copy(unused)
            for _ in range(len(unused_)):
                first = unused_.pop()
                temp_ = copy.copy(temp)
                temp_.append(first)
                per(temp_,unused_)
                unused_.insert(0,first)
        per([],nums)
        return res

if __name__ == "__main__":
    nums = [1,2,3]
    s = Solution()
    print(s.permute(nums))