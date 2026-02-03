#leetcode 3622. Check Divisibility by Digit Sum and Product
# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description/

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ori=n
        add=0
        prod=1
        while n//10!=0:
            i=n%10
            n//=10
            add+=i
            prod*=i
        print(add+n,prod*n)
        return ori%sum([add+n,prod*n])==0