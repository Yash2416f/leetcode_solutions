#leetcode 1404. Number of Steps to Reduce a Number in Binary Representation to One
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution:
    def numSteps(self, s: str) -> int:
        dec=[int(s[a])*(2**(len(s)-a-1)) for a in range(len(s)) ]
        deci=sum(dec)
        count=0
        while deci!=1:
            if deci%2==0:
                deci//=2
                count+=1
            else:
                deci+=1
                count+=1
        return count