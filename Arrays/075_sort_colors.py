#leetcode 75. Sort Colors
# https://leetcode.com/problems/sort-colors/description/

from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        y=Counter(nums)
        nums[:]=[0]*y[0]+[1]*y[1]+[2]*y[2]