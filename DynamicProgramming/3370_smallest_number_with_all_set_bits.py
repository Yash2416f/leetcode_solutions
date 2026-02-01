#leetcode 3370. Smallest Number with All Set Bits
# https://leetcode.com/problems/smallest-number-with-all-set-bits/description/

class Solution:
    def smallestNumber(self, n: int) -> int:
        x=len(bin(n))-2
        return int('1'*x, 2)