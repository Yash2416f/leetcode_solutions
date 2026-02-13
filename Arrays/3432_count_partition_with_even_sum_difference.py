# leetcode 3432. Count Partitions With Even Sum Difference
# https://leetcode.com/problems/count-partitions-with-even-sum-difference/

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-1):
            left=sum(nums[:i+1])
            right=sum(nums[i+1:])
            if (left-right)%2==0:
                # print(left,right)
                c+=1
        return c
