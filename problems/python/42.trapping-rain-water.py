#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # # TC: O(n)
        # # SC: O(1)
        # ans = pre_max = sur_max = 0
        # left, right = 0, len(height)-1
        # while left < right:
        #     pre_max = max(pre_max, height[left])
        #     sur_max = max(sur_max, height[right])
        #     if pre_max < sur_max:
        #         ans += pre_max - height[left]
        #         left += 1
        #     else:
        #         ans += sur_max - height[right]
        #         right -= 1

        # return ans
    
        # TC: O(n)
        # SC: O(min(n, U))
        st = []
        ans = 0
        for i, h in enumerate(height):
            while st and height[st[-1]] < h:
                bottom_h = height[st.pop()]
                if len(st) == 0:
                    break
                left = st[-1]
                dh = min(height[left], h) - bottom_h
                ans += dh * (i - left - 1)
            st.append(i)

        return ans
      
# @lc code=end

