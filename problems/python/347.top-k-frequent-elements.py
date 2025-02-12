#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TC: O(n log n)
        # SC: O(n+k)
        from collections import defaultdict
        import heapq
        ht = defaultdict(int)
        for num in nums:
            ht[num] += 1
        
        ans = []
        for num, freq in ht.items():
            if len(ans) == k:
                heapq.heappushpop(ans, (freq, num))
            else:
                heapq.heappush(ans, (freq, num))
        
        return [num for _, num in ans]
        
# @lc code=end

