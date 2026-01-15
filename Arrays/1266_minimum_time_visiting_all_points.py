#leetcode 1266. Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0

        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]

            time += max(abs(x2 - x1), abs(y2 - y1))

        return time
