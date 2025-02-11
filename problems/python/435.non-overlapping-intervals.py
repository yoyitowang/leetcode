#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # TC: O(n log n)
        # SC: O(1)
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        ans = 0
        min_end = intervals[0][1]
        print(intervals)
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < min_end:
                min_end = min(min_end, end)
                ans += 1
            else:
                min_end = end

        return ans
    
        #
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        ans = 0
        min_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < min_end:
                ans += 1
            else:
                min_end = end


        return ans
# @lc code=end

