#leetCode Problem 342: Power of Four
# https://leetcode.com/problems/power-of-four/description/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n>=4:
            n=n/4
        return n==1
            
        