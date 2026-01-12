#leetcode 020 Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        paren={'[':']',"(":')',"{":"}"}
        sta=[]
        for i in s:
            if i in paren:
                sta.append(i)
            else:
                if len(sta)==0:
                    return False
                if (paren[sta[-1]]==i):
                    sta.pop()
                else:
                    return False
        return sta==[] 