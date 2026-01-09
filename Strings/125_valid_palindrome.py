#leetCode Problem 125: Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        y=s.lower()
        rev=''.join(a for a in y if a.isalnum())
        return rev[::-1]==rev