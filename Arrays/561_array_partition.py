#leetcode 561. Array Partition
# https://leetcode.com/problems/array-partition/description/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num=sorted(nums)
        x=0
        for i in range (0,len(nums),2):
            x+=num[i]
        return x
