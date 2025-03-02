#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # TC: O(n^2)
        # # SC: O(n)
        # ans = [-1] * len(nums1)
        # for i, n1 in enumerate(nums1):
        #     idx = nums2.index(n1)
        #     for j in range(idx+1, len(nums2)):
        #         if nums2[j] > n1:
        #             ans[i] = nums2[j]
        #             break
        # return ans

        # stack
        # TC: O(n)
        # SC: O(n)
        idx = {num: i for i, num in enumerate(nums1)}
        ans = [-1] * len(nums1)
        st = []
        for num in nums2:
            while st and num > st[-1]:
                ans[idx[st.pop()]] = num

            if num in idx:
                st.append(num)
        return ans
# @lc code=end

