'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def __init__(self, nums: List[int]) -> int:
        self.rob(nums)
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        pre_pre_nums = []
        pre_nums = []
        pre_inc = 0
        for index in range(len(nums)):
            if index == 0:
                pre_inc = nums[index]
                pre_pre_nums = [1]
            elif index == 1:
                if nums[0] < nums[index]:
                    pre_inc = nums[index] - nums[index-1]
                    pre_nums = [0,1]
                else:
                    pre_nums = [1,0]
            else:
                temp = pre_nums[:]
                if pre_nums[-1]==0:
                    pre_inc = nums[index]
                    pre_nums = pre_nums+[1]
                elif pre_inc > nums[index]:
                    pre_nums = pre_nums+[0]
                else:
                    pre_inc = nums[index] - pre_inc
                    pre_nums = pre_pre_nums+[0,1]
                pre_pre_nums = temp[:]
        rob_sum = 0
        # print(pre_nums)
        for index,num in enumerate(nums):
            rob_sum += pre_nums[index] * num
        # print(rob_sum)
        return rob_sum
if __name__ == "__main__":
    # nums = [X1,X2,...,Xn-1,Xn] + [Y]
    nums = [2,7,9,3,1]
    s = Solution(nums)