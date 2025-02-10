#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # TC: O(n^2)
        # SC: O(n)
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []

        for p in people:
            res.insert(p[1], p)
        return res     
# @lc code=end

