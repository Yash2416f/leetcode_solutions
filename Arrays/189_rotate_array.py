#leetcode 189. Rotate Array
# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     y=nums.pop()
        #     nums=[y]+nums
        #     print(nums)
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)