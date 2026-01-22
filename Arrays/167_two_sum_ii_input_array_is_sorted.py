#leetcode 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        y=set(numbers)
        z=[[a+1,numbers.index(target-numbers[a])+1] for a in range(len(numbers)) if target-numbers[a] in y]
        if z[0][0]!=z[0][1]:
            return z[0]
        else:
            w=z[0]
            w[1]=numbers.index(numbers[w[0]-1],w[0])+1
            return w