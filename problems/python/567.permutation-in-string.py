#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # # TC: O(n)
        # # SC: O(26)
        # cnt1 = Counter(s1)
        # len1, len2 = len(s1), len(s2)
        # if len1 > len2:
        #     return False
        
        # for i in range(len1, len2+1):
        #     cnt2 = Counter(s2[i-len1: i])
        #     if cnt1 == cnt2:
        #         return True

        # return False

        # TC: O(n)
        # SC: O(26)
        if len(s1) > len(s2):
            return False

        cnt1 = [0]*26 + [1]
        cnt2 = [0]*26 + [1]

        matches = 0
        for i, char in enumerate(s1):
            cnt1[ord(char)-ord('a')] += 1
            cnt2[ord(s2[i])-ord('a')] += 1

        for i in range(26):
            if cnt1[i] == cnt2[i]:
                matches += 1

        for l, r in enumerate(range(len(s1), len(s2))):
            if matches == 26: return True

            idx = ord(s2[l])-ord('a')
            cnt2[idx] -= 1
            if cnt1[idx] == cnt2[idx]:
                matches += 1
            elif cnt1[idx] - 1 == cnt2[idx]:
                matches -= 1

            idx = ord(s2[r])-ord('a')
            cnt2[idx] += 1
            if cnt1[idx] == cnt2[idx]:
                matches += 1
            elif cnt1[idx] + 1 == cnt2[idx]:
                matches -= 1
            
        return matches == 26        
# @lc code=end

