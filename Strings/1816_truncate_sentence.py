#leetcode 1816. Truncate Sentence
# https://leetcode.com/problems/truncate-sentence/description/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        y=s.split()
        t=" ".join(y[i] for i in range(k) if i<k)
        return t
