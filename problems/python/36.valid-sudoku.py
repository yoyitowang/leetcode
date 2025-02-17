#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # TC: O(9x9)
        # SC: O(1)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                box = board[i][j]
                if box == '.':
                    continue
                
                if box in rows[i]:
                    return False
                if box in cols[j]:
                    return False
                idx = (i//3) * 3 + (j//3)
                if box in boxes[idx]:
                    return False
                
                rows[i].add(box)
                cols[j].add(box)
                boxes[idx].add(box)

        return True
                
# @lc code=end

