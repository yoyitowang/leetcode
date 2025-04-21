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

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # 哈希表，映射 key 到节点
        self.size = 0  # 当前缓存大小
        self.capacity = capacity  # 缓存容量
        self.head = DLinkedNode()  # 虚拟头节点
        self.tail = DLinkedNode()  # 虚拟尾节点
        
        # 初始化双向链表
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            newNode = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = newNode
            # 添加至双向链表的头部
            self.addToHead(newNode)
            self.size += 1
            
            # 如果超出容量，删除双向链表的尾部节点
            if self.size > self.capacity:
                # 删除尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        """将节点添加到双向链表的头部"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        """从双向链表中删除一个节点"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def moveToHead(self, node):
        """将节点移动到双向链表的头部"""
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self):
        """删除双向链表的尾部节点，并返回该节点"""
        node = self.tail.prev
        self.removeNode(node)
        return node

# @lc code=end

