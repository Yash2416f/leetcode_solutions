#leetcode 3794. Reverse String Prefix
# https://leetcode.com/problems/reverse-string-prefix/description/

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        y=s[:k]
        return y[::-1]+s[k:]