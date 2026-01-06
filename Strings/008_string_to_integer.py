#leetcode problem number: 8
# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        n=''
        x=s.strip()
        if x=='':
            return 0
        if x[0]=="-" or x[0]=="+":
            n+= x[0]
            for i in range(1,len(x)):
                if x[i].isdigit():
                    n+=  x[i]
                else:
                    break
        
        else:
            for i in range(len(x)):
                if x[i].isdigit():
                    n+=  x[i]
                else:
                    break
        if n == '' or n=="+" or n=="-":
            return 0
        else:
            num=int(n)

        if num < -2**31:
            return -2**31
        elif num > 2**31 - 1:
            return 2**31 - 1
        else:
            return num
