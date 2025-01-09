#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startx = 0
        starty = 0
        loop = mid = n // 2
        res = [[0]*n for _ in range(n)]
        cnt = 1

        for offset in range(1, loop+1):
            # top: left > right
            for i in range(starty, n-offset):
                res[startx][i] = cnt
                cnt += 1

            # right: top > down
            for i in range(startx, n-offset):
                res[i][n-offset] = cnt
                cnt += 1

            # down: right > left
            for i in range(n-offset, starty, -1):
                res[n-offset][i] = cnt
                cnt += 1

            # left: down > top
            for i in range(n-offset, startx, -1):
                res[i][starty] = cnt
                cnt += 1

            startx += 1
            starty += 1
        
        if n % 2 == 1:
            res[mid][mid] = cnt

        return res


        
# @lc code=end

