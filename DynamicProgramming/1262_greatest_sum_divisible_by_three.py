# leetcode 1262. Greatest Sum Divisible by Three
# https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        total=sum(nums)
        rem1=[i for i in nums if i%3==1]
        rem2=[j for j in nums if j%3==2]
        if total%3==1:
            remove=float("inf")
            if len(rem1) >= 1:
                remove = rem1[0]
            if len(rem2) >= 2:
                remove = min(remove, rem2[0] + rem2[1])
            return total-remove if (total-remove)>0 else 0
        elif total%3==2:
            remove=float("inf")
            if len(rem2) >= 1:
                remove = rem2[0]
            if len(rem1) >= 2:
                remove = min(remove, rem1[0] + rem1[1])
            return total-remove if remove!=float('inf') else 0
        else:
            return total