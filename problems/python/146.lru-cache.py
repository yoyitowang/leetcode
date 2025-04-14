#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    __slot__ = ('prev', 'next', 'key', 'val')

    def __init__(self, key=0, val=0):
        self.key=key
        self.val=val
    
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get_node(self, key: int) -> Node:
        if key not in self.cache:
            return None
        # get val
        node = self.cache[key]
        # remove and push front
        self.remove(node)
        self.push_front(node)

        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.val = value
            return
        self.cache[key] = node = Node(key, value)
        self.push_front(node)
        if len(self.cache) > self.capacity:
            back_node = self.dummy.prev
            del self.cache[back_node.key]
            self.remove(back_node)
            
    def remove(self, x: Node):
        x.prev.next = x.next
        x.next.prev = x.prev

    def push_front(self, x: Node):
        x.next = self.dummy.next
        x.prev = self.dummy
        x.prev.next = x
        x.next.prev = x

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

