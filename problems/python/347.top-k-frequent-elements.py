#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TC: O(n logn)
        # SC: O(k)
        from collections import defaultdict
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        prior_que = []
        counter = sorted(counter.items(), key=lambda x:x[1], reverse=True) # TC: O(n logn)
        res = []
        for i in range(k):
            res.append(counter[i][0]) # TC: O(k)
        return res     
# @lc code=end

