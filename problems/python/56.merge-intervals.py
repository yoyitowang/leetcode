#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # TC: O(n log n)
        # SC: O(n log n) for stack of sorting
        intervals.sort(key=lambda x: x[0])
        ans = []
        if not intervals:
            return ans

        ans.append(intervals[0])

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if ans[-1][1] >= start:
                prev = ans.pop()
                merged = [prev[0], max(prev[1], end)]
                ans.append(merged)
            else:
                ans.append(intervals[i])
        return ans
    
# @lc code=end

