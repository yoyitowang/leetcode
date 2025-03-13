#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # TC: O(n logn)
        # SC: O(n)

        time = [0] * len(position)
        for i, [pos, sp] in enumerate(sorted(zip(position, speed))):
            time[i] = (target-pos)/sp

        st = []
        for t in time:
            while st and t >= st[-1]:
                st.pop()
            st.append(t)

        return len(st)
        
# @lc code=end

