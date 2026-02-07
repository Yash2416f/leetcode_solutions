# leetcode 3168. Minimum Number of Chairs in a Waiting Room
# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description/
class Solution:
    def minimumChairs(self, s: str) -> int:
        c=0
        maxi=0
        for i in s:
            if i=='E':
                c+=1
                if c>maxi:
                    maxi=c
            elif i=='L':
                c-=1
        return maxi

