#leetcode problem: 961. N-Repeated Element in Size 2N Array
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num!=0:
            if num%2==0:
                num/=2
            else:
                num-=1
            count+=1
        return count