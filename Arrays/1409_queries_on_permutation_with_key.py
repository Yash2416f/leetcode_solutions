#leetcode 1409 Queries on a Permutation With Key
# https://leetcode.com/problems/queries-on-a-permutation-with-key/description/

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p=[x for x in range(1,m+1)]
        z=[]
        for i in range(len(queries)):
    
            try:
                x=p.index(queries[i])
            except ValueError:
                continue
            
            z.append(x)
            
            y=p.pop(x)

            p=[y]+p
            
        return z


        