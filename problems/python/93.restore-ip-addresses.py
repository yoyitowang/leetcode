#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # TC: O(3^4=81) = O(1)
        # SC: O(4) = O(1)
        self.ans = []

        def backtracking(start, path):
            n = len(path)
            ns = len(s)

            if n == 4 and start != ns:
                return
            elif start == ns:
                if n == 4:
                    self.ans.append(".".join(path[:]))
                return
            
            for i in range(start, ns):
                ip, post = s[start: i+1], s[i+1: ]
                if (4-n) * 3 < len(post):
                    return
                if self.isValid(s, start, i+1):
                    path.append(ip)
                    backtracking(i+1, path)
                    path.pop()

        backtracking(0, [])    
        return self.ans
        
    def isValid(self, s, start, end):
        if start > end:
            return False
        
        if s[start] == '0' and end - start > 1:
            return False
        
        if int(s[start:end]) > 255:
            return False

        return True
            
# @lc code=end

