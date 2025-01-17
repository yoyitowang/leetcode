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
        self.cur = self.q1

    def push(self, x: int) -> None:
        self.refresh()
        self.cur.append(x)

    def pop(self) -> int:
        self.refresh()
        for _ in range(len(self.cur)-1):
            self.cur.append(self.cur.popleft())
        return self.cur.popleft()

    def top(self) -> int:
        self.refresh()
        for _ in range(len(self.cur)-1):
            self.cur.append(self.cur.popleft())
        num = self.cur.popleft()
        self.cur.append(num)
        return num
        

    def empty(self) -> bool:
        return not (self.q1 or self.q2)
        
    def refresh(self):
        if not self.empty():
            if len(self.q1) > 0:
                self.cur = self.q1
            else:
                self.cur = self.q2

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

