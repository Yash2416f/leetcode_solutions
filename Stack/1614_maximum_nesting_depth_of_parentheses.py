# leetcode 1614. Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

class Solution:
    def maxDepth(self, s: str) -> int:
        sta=[]
        maxi=0
        for i in s:
            if i=='(':
                sta.append(i)
                if len(sta)>maxi:
                    maxi=len(sta)
            elif i==')':
                sta.pop()
        return maxi
