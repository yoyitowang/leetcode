#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # TC: O(n log n + k)
        # SC: O(1)
        nums.sort() # O(n log n)
        idx = 0
        while k > 0:
            if idx < len(nums) and nums[idx] < 0:
                nums[idx] = -nums[idx]
                idx += 1
            else:
                if k % 2 == 0:
                    break
                else:
                    nums.sort()
                    nums[0] = -nums[0]
                    break
            k -= 1
        
        return sum(nums)      
# @lc code=end

