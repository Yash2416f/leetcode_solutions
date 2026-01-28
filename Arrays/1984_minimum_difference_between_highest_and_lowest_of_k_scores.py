# leetcode 1984. Minimum Difference Between Highest and Lowest of K Scores
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        arr=[ abs(nums[i] - nums[i+k-1]) for i in range(0,len(nums)-k+1)]
        return min(arr)


