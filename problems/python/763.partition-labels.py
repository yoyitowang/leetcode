#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # TC: O(n)
        # SC: O(26)=O(1)

        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i

        ans = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last_index[char])
            if i == end:
                ans.append(end-start+1)
                start = i + 1
        
        return ans  
# @lc code=end

