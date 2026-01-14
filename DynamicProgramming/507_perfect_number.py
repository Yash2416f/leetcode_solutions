#leetcode 507. Perfect Number
# https://leetcode.com/problems/perfect-number/description/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if (num<=1):
            return False
        pairs = [sum([i, num // i]) for i in range(1, int(num**0.5) + 1) if num % i == 0]

        # print(sum(pairs))
        return sum(pairs)-num==num