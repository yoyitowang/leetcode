#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        n = len(gas)
        total = cur = ans = 0

        for i in range(n):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                ans = i + 1
                cur = 0
        
        if total < 0:
            return -1
        return ans                
# @lc code=end

