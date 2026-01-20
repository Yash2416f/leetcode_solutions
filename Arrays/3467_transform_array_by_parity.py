#leetcode 3467. Transform Array by Parity
# https://leetcode.com/problems/transform-array-by-parity/description/

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        x=[]
        for i in nums:
            if i%2==0:
                x.append(0)
            else:
                x.append(1)
        return sorted(x)
