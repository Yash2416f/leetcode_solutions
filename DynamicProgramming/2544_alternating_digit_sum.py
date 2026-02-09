# leetcode 2544. Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum/description/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        y=str(n)
        f=[]
        # f=[(int(y[i]),int(y[i])*-1) for i in range(len(y)) if i%2==0 else i%2==1]
        for i in range(len(y)):
            if i%2==0:
                f.append(int(y[i]))
            else:
                f.append(int(y[i])*-1)
        return sum(f) 

    