#leetcode 66. Plus One
# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=''
        for i in digits:
            num+=str(i)
        x=int(num)+1
        return[int(i) for i in str(x)]