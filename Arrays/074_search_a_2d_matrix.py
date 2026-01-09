#leetcode 74: Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li=[i for row in matrix for i in row]
        set_list=set(li)
        return target in set_list