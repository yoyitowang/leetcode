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
        
        # n = len(stones)
        # total = sum(stones)
        # cap = total//2

        # @cache
        # def dfs(i, c):
        #     if i < 0:
        #         return abs(total-c-c)
                
        #     p1 = dfs(i-1, c+stones[i])
        #     p2 = dfs(i-1, c)

        #     return min(p1, p2)
            
        # return dfs(n-1, 0)

        # dp-array
        # TC: O(n*target)
        # SC: O(n*target)
        n = len(stones)
        total = sum(stones)
        if total/2 <= (m:=max(stones)):
            return abs(total - 2*m)

        target = total//2
        dp = [[False] * (target+1) for _ in range(n+1)]
        dp[0][0] = True

        for i, x in enumerate(stones):
            for j in range(target+1):
                if stones[i] > j:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j] | dp[i][j-x]
        ans = total
        for j in range(target, -1, -1):
            if dp[n][j]:
                ans = total - 2*j
                break

        return ans
# @lc code=end

