#leetcode problem number: 3121 count the number of special characters ii
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        y=set(word)
        f=[i for i in word if chr(ord(i)-32) in y]
        print(f)
        j=[k for k in f if k not in word[word.index(k.upper()):]]
        return len(set(j))