# leetcode 3019. Number of Changing Keys
# https://leetcode.com/problems/number-of-changing-keys/description/

class Solution:
    def countKeyChanges(self, s: str) -> int:
        y=[i for i in range(len(s)-1) if abs(ord(s[i])-ord(s[i+1]))!=0 and abs(ord(s[i])-ord(s[i+1]))!=32]
        print(y)
        return len(y)
        # y=s.lower()
        # z=set(y)
        # return len(z)-1
