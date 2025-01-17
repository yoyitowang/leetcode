#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        _next = self.build_next(needle)
        if not needle:
            return 0

        i = j = 0
        while i < len(haystack):
            s1 = haystack[i]
            s2 = needle[j]
            # matched
            if s1 == s2:
                i += 1
                j += 1
            # not matched -> check _next and go back
            else:
                if j > 0:
                    j = _next[j-1]
                else:
                    i += 1

            if j == len(needle):
                return i - j
        return -1

    def build_next(self, patt: str):
        next = [0]  # 初始化 Next 陣列
        prefix_len = 0  # 前綴和後綴的最大相同長度
        i = 1  # 從第二個字元開始計算

        while i < len(patt):
            if patt[prefix_len] == patt[i]:  # 如果匹配成功
                prefix_len += 1  # 前綴長度加 1
                next.append(prefix_len)  # 將結果加入 Next 陣列
                i += 1
            else:  # 匹配失敗
                if prefix_len > 0:  # 如果前綴長度大於 0，嘗試回退
                    prefix_len = next[prefix_len - 1]
                else:  # 如果前綴長度為 0，無法回退
                    next.append(0)
                    i += 1

        return next
        

# @lc code=end

