#leetcode 026 Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        ex_nums=[]
        for i in nums:
            if i not in ex_nums:
                ex_nums.append(i)
        nums[:]=ex_nums