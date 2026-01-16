#leetcode 2000. Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/description/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        y=word.find(ch)
        if y!=-1:
            n=word[:y+1]
            new=n[::-1]
            old=word[y+1:]
            return new+old
        else:
            return word