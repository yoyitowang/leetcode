#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # TC: O(n*log(M))
        # SC: O(1)
        import math
        piles.sort()
        n = max(piles)
        left, right = 1, n
        ans = 0
        while left <= right:
            mid = left + (right-left)//2
            cur = 0
            for pile in piles:
                cur += math.ceil(pile/mid)
                if cur > h:
                    break

            if cur <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
# @lc code=end

