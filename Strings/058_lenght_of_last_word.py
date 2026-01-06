#leetcode problem 58
# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y=s.split()
        return len(y[-1])