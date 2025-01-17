#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        from collections import deque
        # last in first out
        self.q1 = deque([])
        self.q2 = deque([])

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        num = self.q1.popleft()
        self.swap()

        return num

    def top(self) -> int:
        if self.empty():
            return
        while len(self.q1) > 0:
            self.q2.append((num:=self.q1.popleft()))
        self.swap()

        return num
        

    def empty(self) -> bool:
        return not self.q1 

    def swap(self):
        self.q1, self.q2 = self.q2, self.q1
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

