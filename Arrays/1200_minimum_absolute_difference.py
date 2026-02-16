# leetcode 1200: Minimum Absolute Difference
# https://leetcode.com/problems/minimum-absolute-difference/description/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min=float(inf)
        for a in range (0, len(arr)-1):
            if arr[a+1]-arr[a] < min:
                min=arr[a+1]-arr[a]
        f=[[arr[i],arr[i+1]] for i in range(len(arr)-1) if arr[i+1]-arr[i]==min]
        return f
