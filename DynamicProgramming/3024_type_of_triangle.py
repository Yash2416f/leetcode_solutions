# leetcode 3024: Type of Triangle
# https://leetcode.com/problems/type-of-triangle/description/

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if max(nums)<sum(nums)-max(nums):

            if nums[1]==nums[2]==nums[0]:
                return "equilateral"
            elif nums[1]!=nums[2]!=nums[0]!=nums[1]:
                return "scalene"
            else:
                return "isosceles"
        return "none"