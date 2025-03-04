#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # TC: O(n+n)
        # SC: O(n+n)
        n = len(heights)
        left = [-1] * n
        st = []
        
        for i, h in enumerate(heights):
            while st and h <= heights[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        
        right = [n] * n
        st.clear()
        for i in range(n-1, -1, -1):
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r-l-1))
        return ans 
# @lc code=end

