# leetcode 233. Number of Digit One
# https://leetcode.com/problems/number-of-digit-one/description/

class Solution:
    def countDigitOne(self, n: int) -> int:
        # c=0
        # for i in range(n+1):
        #     if '1' in str(i):
        #         c+= str(i).count('1')
        # return c

        count = 0
        factor = 1
        
        while factor <= n:
            lower = n % factor
            cur = (n // factor) % 10
            higher = n // (factor * 10)
            
            if cur == 0:
                count += higher * factor
            elif cur == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor
            
            factor *= 10
        
        return count