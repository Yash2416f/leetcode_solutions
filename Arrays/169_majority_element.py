#leetcode problem 169. Majority Element
# https://leetcode.com/problems/majority-element/description/

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=count.most_common() #most_common returns the list of tuples of elements with their count from highest to lowest if no arguement is given other returns n most common elemens
        return ans[0][0] #list of tuple (ans looks something like this----> [(3,2),(2,1)]    )