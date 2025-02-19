#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # sum = n1 + n2
        # n1 <= (sum)/2
        n = len(stones)
        total = sum(stones)
        cap = total//2

        @cache
        def dfs(i, c):
            if i < 0:
                return abs(total-c-c)
                
            p1 = dfs(i-1, c+stones[i])
            p2 = dfs(i-1, c)

            return min(p1, p2)
            
        return dfs(n-1, 0)
# @lc code=end

