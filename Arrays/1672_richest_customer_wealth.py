#leetcode problem 1672: Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=0
        for m in accounts:
            total=sum(m)
            if total>max:
                max=total
        return max