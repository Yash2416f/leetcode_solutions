#leetcode problem number: 191 number of 1 bits
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)
        j=[i for i in b if i =='1']
        return len(j)