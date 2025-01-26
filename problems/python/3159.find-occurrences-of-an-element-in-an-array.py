#
# @lc app=leetcode id=3159 lang=python3
#
# [3159] Find Occurrences of an Element in an Array
#

# @lc code=start
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        # TC: O(n+m)
        # SC: O(t)
        res = []
        ht = {x: []}
        for idx, num in enumerate(nums):
            if num == x:
                ht[num].append(idx)
        for query in queries:
            if query <= len(ht[x]):
                res.append(ht[x][query-1])
            else:
                res.append(-1)
        return res   
# @lc code=end

