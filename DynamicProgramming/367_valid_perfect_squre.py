#leetcode 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/description/

import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        y=math.isqrt(num)
        return y*y==num