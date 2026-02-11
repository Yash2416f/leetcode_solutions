# leetcode 3719. Longest Balanced Subarray I
# https://leetcode.com/problems/longest-balanced-subarray-i/description/

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            odd = set()
            even = set()
            
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                
                if len(odd) == len(even):
                    ans = max(ans, j - i + 1)
        
        return ans

    #     all_subarrays = [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)]
    #     a=[x for x in all_subarrays if self.oddEven(x)==True]
    #     if not a:
    #         return 0
    #     else:
    #         return len(max(a, key=len))
    # def oddEven(self,arr):
    #     y=set(arr)
    #     f=[i for i in y if i%2==0]
    #     return len(y)-len(f)==len(f)
