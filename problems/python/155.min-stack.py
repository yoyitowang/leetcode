#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.st = []
        self.st_min = []

    def push(self, val: int) -> None:
        self.st.append(val)
        self.st_min.append(min(self.st_min[-1] if self.st_min else val, val))

    def pop(self) -> None:
        self.st.pop()
        self.st_min.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.st_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

