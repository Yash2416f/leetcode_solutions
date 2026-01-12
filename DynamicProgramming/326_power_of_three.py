#leetcode 326. Power of Three
# https://leetcode.com/problems/power-of-three/description/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n>=3:
            n=n/3
        return n==1