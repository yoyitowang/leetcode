#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True  # 邊界情況，1 是完全平方數
        
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:  # 找到完全平方數
                return True
            elif square < num:  # 繼續搜索右半部分
                left = mid + 1
            else:  # 繼續搜索左半部分
                right = mid - 1
        
        return False  # 未找到完全平方數

        
# @lc code=end

