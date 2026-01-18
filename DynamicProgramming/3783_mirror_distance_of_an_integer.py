#leetcode 3783. Mirror Distance of an Integer
# https://leetcode.com/problems/mirror-distance-of-an-integer/description/

class Solution:
    def mirrorDistance(self, n: int) -> int:
        r=str(n)[::-1]
        return abs(n- int(r))