# leetcode problem 283: Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)

        for _ in range(count):
            nums.remove(0)
            nums.append(0)
