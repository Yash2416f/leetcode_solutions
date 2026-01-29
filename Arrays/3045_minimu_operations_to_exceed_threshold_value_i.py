#leetcode 3045. Minimum Operations to Exceed Threshold Value I
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        c=0
        while k>nums[0]:
            nums.pop(0)
            c+=1
        return c