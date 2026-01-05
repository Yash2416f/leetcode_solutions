# leetcode problem 4: Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=[]
        num=nums1+nums2
        sorted_arr=sorted(num)
        if len(sorted_arr)%2!=0:
            mid=sorted_arr[(len(sorted_arr)//2)]
        else:
            mid=(sorted_arr[(len(sorted_arr)//2)-1]+sorted_arr[(len(sorted_arr)//2)])/2
        return mid