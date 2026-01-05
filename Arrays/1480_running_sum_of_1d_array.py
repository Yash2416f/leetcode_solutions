#leetcode 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=[]
        for i in range (len(nums)):
            if i==0:
                sums.append(nums[i])
            else:
                sums.append(sums[i-1]+nums[i])
        return sums
