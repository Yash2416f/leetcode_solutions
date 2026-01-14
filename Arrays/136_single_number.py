#leetcode 136. Single Number
# https://leetcode.com/problems/single-number/description/

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # s=[i for i in nums if nums.count(i)==1]
        # return s[0]
        count=Counter(nums)
        y=count.most_common()
        print(y)
        return y[-1][0]
