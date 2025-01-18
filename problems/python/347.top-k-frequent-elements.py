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
        from collections import Counter
        from heapq import heappush, heappop
        counter = Counter(nums) # O(n)

        min_heap = [] # O(k)
        for num, freq in counter.items(): # O(n)
            heappush(min_heap, (freq, num)) # O(n log n)
            if len(min_heap) > k:
                heappop(min_heap) # O(log n)
        
        return [num for freq, num in min_heap]    
# @lc code=end

