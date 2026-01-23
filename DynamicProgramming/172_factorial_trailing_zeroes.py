#leetcode 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        divisor = 5

        while divisor <= n:
            count += n // divisor
            divisor *= 5

        return count
        # f=1
        # for i in range(1,n+1):
        #     f=f*i
        # j=str(f)
        # if j=='0':
        #     return 0
        # else:
        #     a=0
        #     for x in range(len(j)-1,-1,-1):
        #         if j[x]=='0':
        #             a+=1
        #         else:
        #             break
        #     return a