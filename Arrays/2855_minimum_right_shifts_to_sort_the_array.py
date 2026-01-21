#leetcode 2855. Minimum Right Shifts to Sort the Array
# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        arranged=sorted(nums)
        count=0
        for i in range(len(nums)):
            if nums==arranged:
                return count
            y=nums.pop()
            nums=[y]+nums
            count+=1
        else:
            return -1