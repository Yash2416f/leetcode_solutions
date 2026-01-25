#leetcode problem 202: Happy Number
# https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSq(num):
            y=str(num)
            f=[int(i)**2 for i in y]
            return sum(f)
        z=set()
        new=sumSq(n)
        
        while new not in z and new!=1:
            z.add(new)
            new=sumSq(new)
        return new==1