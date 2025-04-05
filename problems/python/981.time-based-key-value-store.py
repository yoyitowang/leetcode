#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.kv:
            return res
        if timestamp < self.kv[key][0][0]:
            return res

        pairs = self.kv[key]
        _, value = self.binary_search(pairs, timestamp)

        return value

    def binary_search(self, pairs: list, timestamp: int):
        n = len(pairs)
        if n == 1:
            return pairs[0]
        left, right = -1, n
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            ts, val = pairs[mid]
            if ts <= timestamp:
                left = mid
            else:
                right = mid
        return pairs[left]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

