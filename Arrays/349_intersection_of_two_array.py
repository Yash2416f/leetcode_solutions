#leetcode 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums1)
        t=set(nums2)
        return [x for x in s if x in t]