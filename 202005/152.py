from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def mp(nums):
            if len(nums)==1:
                return nums[0]
            buff1 = 0
            buff2 = 0
            neg = 1
            i = 0
            while i < len(nums):
                if nums[i] > 0:
                    if buff1 ==0:
                        buff1 = nums[i]
                    else:
                        buff1*= nums[i]
                    i+=1
                elif nums[i] == 0:
                    i+=1
                    if i==len(nums):
                        return max(buff1,buff2)
                    elif neg<0:
                        return max(buff1,neg,mp(nums[i:]))
                    return max(max(buff1,buff2),mp(nums[i:]))
                elif nums[i] < 0:
                    neg = nums[i]
                    i+=1
                    while i<len(nums) and nums[i] > 0:
                        if buff2 == 0:
                            buff2 = nums[i]
                        else:
                            buff2*=nums[i]
                        i+=1
                    if i<len(nums) and nums[i] < 0:
                        if buff2==0 :
                            buff2 = 1
                        if buff1 == 0:
                            buff1 = 1
                        buff1 = buff1*buff2*neg*nums[i]
                        buff2 = 0
                        neg = 1
                        i+=1
            if buff2==0:
                buff2=1
            if neg < 0:
                return max(buff1,buff2)
            else:
                return buff1*buff2
        return mp(nums)

                    



if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2,-5,-2,-4,3]))
