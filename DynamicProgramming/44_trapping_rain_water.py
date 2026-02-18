# leetcode 44: Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1

        return water

        # water = []
        # n = len(height)

        # for i in range(n):
        #     left_max = max(height[:i]) if i > 0 else 0
        #     right_max = max(height[i+1:]) if i < n-1 else 0
        #     water.append(max(0, min(left_max, right_max) - height[i]))
            

        # return sum(water)
