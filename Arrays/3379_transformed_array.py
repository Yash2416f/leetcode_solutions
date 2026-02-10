# leetcode 3379. Transformed Array
# https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        y=[]
        for i in range(n):
            x=nums[i]
            ans=(i+x)%(n)
            if ans>n-1:
                y.append(nums[ans-n])
            else:
                y.append(nums[ans])
        print(y)  
        return y      
