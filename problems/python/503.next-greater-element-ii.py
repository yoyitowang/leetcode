#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # TC: O(n*2)
        # TC: O(n)
        ans = [-1] * len(nums)
        st = []

        for i, num in enumerate(nums):
            while st and nums[st[-1]] < num:
                ans[st.pop()] = num
            st.append(i)
        for i, num in enumerate(nums):
            # st is empty: no more need to be updated -> return
            if not st:
                return res
            while st and nums[st[-1]] < num:
                ans[st.pop()] = num
            st.append(i)

        return ans
# @lc code=end

