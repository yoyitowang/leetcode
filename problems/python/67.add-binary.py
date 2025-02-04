#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # TC: O(n)
        # SC: O(n)
        la, lb = len(a), len(b)
        diff = abs(lb-la)
        if la > lb:
            b = "0" * diff + b
        else:
            l = len(a)
            a = "0" * diff + a
        
        acc = 0
        ans = ""
        for i in range(len(a)-1, -1, -1):
            res = int(a[i]) + int(b[i]) + acc
            acc = res // 2
            res %= 2
            ans = str(res) + ans
        if acc > 0:
            ans = "1" + ans

        return ans
                   
# @lc code=end

