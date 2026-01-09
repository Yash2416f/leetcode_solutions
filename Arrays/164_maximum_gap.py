#leetcode 164. Maximum Gap
# https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        else:
            y=sorted(nums)
            max=y[1]-y[0]
            for i in range(0, len(y)-1):
                num= y[i+1]-y[i]
                if num>max:
                    max=num
            return max