#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        # first in last out
        self.st_in = []
        self.st_out = []

    def push(self, x: int) -> None:
        self.st_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return 
        self.update()

        return self.st_out.pop()

    def peek(self) -> int:
        self.update()
        return self.st_out[-1]

    def empty(self) -> bool:
        return not (self.st_in or self.st_out)

    def update(self) -> None:
        if not self.empty() and len(self.st_out) == 0:
            while self.st_in:
                self.st_out.append(self.st_in.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

