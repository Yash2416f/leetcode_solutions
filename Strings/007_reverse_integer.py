#leetcode 007. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        y=str(x)
        z=y[::-1]
        if z.endswith('+') or z.endswith('-'):
            w='-'+ z[0:len(z)-1]
            if int(w)<-2**31 or int(w)>2**31-1:
                return 0
            else:
                return int(w)
        else:
            if int(z)<-2**31 or int(z)>2**31-1:
                return 0
            else:
                return int(z)