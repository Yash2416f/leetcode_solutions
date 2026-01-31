# leetcode problem 1512:number of good pairs
# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num=[[i,j] for i in range(len(nums)-1) for j in range(i+1, len(nums)) if nums[i]==nums[j]]
        print(num)
        return len(num)