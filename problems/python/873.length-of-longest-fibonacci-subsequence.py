#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # TC: O(n^2)
        # SC: O(n^2)
        # f[(2, 3)] = f[(1, 2)] + 1
        # f[(j, i)] = f[(k, j)] + 1
        # arr[k] + arr[j] = arr[i], k < j < i
        arrSet = set(arr)
        n = len(arr)
        f = {}
        ans = 0

        for i in range(n):
            for j in range(i):
                diff = arr[i] - arr[j]
                if diff in arrSet and diff < arr[j]:
                    f[(arr[j], arr[i])] = f.get((diff, arr[j]), 2) + 1
                    ans = max(ans, f[(arr[j], arr[i])])
        
        return ans
# @lc code=end

