#leetcode 3271. Hash Divided String
# https://leetcode.com/problems/hash-divided-string/description/

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n_sub=len(s)//k
        ch=''
        for i in range(n_sub):
            a=s[k*i:k*(i+1)]
            add=[ord(j)-97 for j in a]
            ch=ch+(chr(sum(add)%26+97))
        return ch