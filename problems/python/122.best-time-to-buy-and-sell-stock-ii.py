#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        ans = 0
        
        for i in range(1, len(prices)):
            if (profit := prices[i] - prices[i-1]) > 0:
                ans += profit
        
        return ans      
# @lc code=end

