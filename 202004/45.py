from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        # dp = [-1 for _ in nums]
        # dp[0],dp[1] = 0,1
        rest = nums[0]
        step,current = 0,0
        while True :
            if current + rest >= len(nums)-1:
                return step+1
            else:
                step += 1
                max_index = current
                while True:
                    current+=1
                    rest -= 1
                    if rest < 0 :
                        break
                    if nums[current]+current >= nums[max_index]+max_index:
                        max_index = current
                rest = nums[max_index]
                current = max_index

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    nums = [2,1,1,1,4]
    nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    s = Solution()
    print(s.jump(nums))