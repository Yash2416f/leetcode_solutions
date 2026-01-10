#leetcode 819. Most Common Word
# https://leetcode.com/problems/most-common-word/description/

from collections import Counter
import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # p=''.join(j for j in paragraph if j not in string.punctuation)
        p=''
        for j in paragraph:
            if j not in string.punctuation:
                p+=j
            else:
                p+=" "
        para=(p.lower()).split()
        ban=set(banned)
        l= [i for i in para if i not in ban]

        count=Counter(l)
        return count.most_common(1)[0][0]
