#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # TC: O(n)
        # # SC: O(n)
        # n = len(temperatures)
        # ans = [0] * n
        # st = []
        # for i, t in enumerate(temperatures):
        #     while st and temperatures[st[-1]] < t:
        #         j = st.pop()
        #         ans[j] = i-j
        #     st.append(i)

        # return ans
    
        # TC: O(n)
        # SC: O(min(n, U))
        n = len(temperatures)
        ans = [0] * n 
        st = []
        for i in range(n-1, -1, -1):
            t = temperatures[i]
            while st and temperatures[st[-1]] <= t:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)

        return ans

# @lc code=end

