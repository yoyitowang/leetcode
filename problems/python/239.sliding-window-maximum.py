#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = Queue(k)
        for i in range(k):
            q.push(nums[i])
        res =[q.front()]        
        
        for i in range(k, len(nums)):
            q.pop(nums[i-k])
            q.push(nums[i])
            res.append(q.front())

        return res

class Queue:
    def __init__(self, k):
        from collections import deque
        self.dq = deque([])

    def pop(self, x):
        if self.dq and self.dq[0] == x:
            self.dq.popleft()

    def push(self, x):
        while self.dq and x > self.dq[-1]:
            self.dq.pop()
        self.dq.append(x)
        
    def front(self) -> int:
        return self.dq[0]

              
# @lc code=end

