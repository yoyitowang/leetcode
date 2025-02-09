#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        from collections import defaultdict, deque
        graph = defaultdict(deque)
        for _from, _to in sorted(tickets):
            graph[_from].append(_to)

        def backtracking(node):
            while graph[node]:
                next_node = graph[node].popleft()
                backtracking(next_node)
            ans.append(node)

        backtracking("JFK")
        return ans[::-1]
   
# @lc code=end

