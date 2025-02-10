#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # TC: O(n)
        # SC: O(1)
        total = defaultdict(int)
        for bill in bills:
            if bill == 10:
                if total[5] < 1:
                    return False
                total[5] -= 1
            elif bill == 20:
                # 5 + 10 or 5 + 5 + 5
                if total[10] >= 1 and total[5] >= 1:
                    total[5] -= 1
                    total[10] -= 1
                elif total[5] >= 3:
                    total[5] -= 3
                else:
                    return False
                
            total[bill] += 1
        
        return True
      
# @lc code=end

