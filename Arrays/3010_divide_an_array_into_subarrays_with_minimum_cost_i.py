#leetcode 3010. Divide an Array Into Subarrays With Minimum Cost I
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        num=sorted(nums[1:])
        return nums[0]+num[1]+num[0]