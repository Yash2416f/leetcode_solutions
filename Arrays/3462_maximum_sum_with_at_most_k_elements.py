# leetcode 3462. Maximum Sum With At Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        print(grid)
        f=[i.sort(reverse=True) for i in grid]
        result = [item for grid, limits in zip(grid, limits) for item in grid[:limits]]
        result.sort(reverse=True)
        print(result)
        return sum(result[:k])