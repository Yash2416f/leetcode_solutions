# leetcode 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        high=len(letters)-1
        low=0
        if letters[-1]<=target or letters[0]>target:
            return letters[0]
        else:
            low, high = 0, len(letters)

        while low < high:
            mid = (low + high) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return letters[low]
        