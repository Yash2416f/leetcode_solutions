#leetcode 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        num=f'{n:032b}'
        # print(num,num[::-1])
        deci=int(num[::-1],2)
        return deci