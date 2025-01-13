#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                from collections import defaultdict, deque
        ht = defaultdict(deque)
        for idx, num in enumerate(nums):
            ht[num].append(idx)

        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            if (_sum := nums[left] + nums[right]) == target:
                return [ht[nums[left]].popleft(), ht[nums[right]].popleft()]
            elif _sum < target:
                left += 1
            else:
                right -= 1
# @lc code=end

