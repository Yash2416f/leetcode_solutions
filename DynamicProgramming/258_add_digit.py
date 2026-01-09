#leetcode problem 258: Add Digits
# https://leetcode.com/problems/add-digits/description/

class Solution:
    def addDigits(self, num: int) -> int:
        while num//10!=0:
            z=0
            for i in str(num):
                z+= int(i)
            num=z
        return num