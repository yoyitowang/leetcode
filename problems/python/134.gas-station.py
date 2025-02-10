#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # TC: O(n)
        # SC: O(n)
        n = len(gas)
        diff = [0] * n
        for i in range(n):
            diff[i] = gas[i] - cost[i]

        if sum(diff) < 0:
            return -1

        acc = 0
        ans = 0
        for i in range(n):
            acc += diff[i]
            if acc < 0:
                acc = 0
                ans = i + 1
        return ans                
# @lc code=end

