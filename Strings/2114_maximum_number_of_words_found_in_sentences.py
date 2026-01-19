#leetcode 2114. Maximum Number of Words Found in Sentences
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        y=[len(i.split(" ")) for i in sentences]
        return max(y)