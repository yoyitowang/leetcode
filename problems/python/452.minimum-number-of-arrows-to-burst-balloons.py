#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # TC: O(n log n)
        # SC: O(1)
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrow = 1
        arrow_point = points[0][1] # set first arrow at the last position of first point

        for start, end in points:
            if arrow_point < start:
                arrow += 1
                arrow_point = end
        
        return arrow
    
        # TC: O(n log n)
        # SC: O(1)
        if not points:
            return 0

        points.sort(key=lambda x: x[0])

        arrow = 1
        arrow_point = points[0][1]
        
        for i in range(1, len(points)):
            start, end = points[i]
            if start > arrow_point:
                arrow += 1
                arrow_point = end
            else:
                arrow_point = min(arrow_point, end)

        return arrow
                   
# @lc code=end

