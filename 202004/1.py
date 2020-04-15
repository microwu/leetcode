from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,num in enumerate(nums):
            hashmap[num] = i
        for i in range(len(nums)):
            if target-nums[i] in hashmap and hashmap[target-nums[i]] != i:
                print([i,hashmap[target-nums[i]]])
                return [i,hashmap[target-nums[i]]]
            

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    s.twoSum(nums,target)