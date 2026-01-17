#leetcode 2161. Partition Array According to Given Pivot
# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pi=[]
        low=[]
        high=[]
        for i in nums:
            if i>pivot:
                high.append(i)
            elif i<pivot:
                low.append(i)
            else:
                pi.append(i)
        return low+pi+high