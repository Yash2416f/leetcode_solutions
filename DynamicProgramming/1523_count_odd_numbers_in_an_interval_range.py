#leetcode 1523. Count Odd Numbers in an Interval Range
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high-low)%2==1 or (high%2==1 and low%2==1):
            return (high-low)//2+1
        elif high%2==0 and low%2==0:
            return (high-low)//2
        