# leetcode 1935. Maximum Number of Words You Can Type
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        y=set(brokenLetters)
        # print(y)
        words=text.split()
        f=[]
        for word in words:
            x=set(word).intersection(y)
            if not x:
                f.append(x)
        return len(f)

         