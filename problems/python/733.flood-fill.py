#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nrow = len(image)
        ncol = len(image[0])
        tcolor = image[sr][sc]

        if tcolor == color:
            return image

        st = deque([[sr, sc]])
        while st:
            r, c = st.popleft()
            if image[r][c] != color:
                image[r][c] = color
            # up
            if (rr := r - 1) >= 0 and image[rr][c] == tcolor:
                st.append([rr, c])
                image[rr][c] = color
            # down
            if (rr := r + 1) < nrow and image[rr][c] == tcolor:
                st.append([rr, c])
                image[rr][c] = color
            # left
            if (cc := c - 1) >= 0 and image[r][cc] == tcolor:
                st.append([r, cc])
                image[r][cc] = color
            # right
            if (cc := c + 1) < ncol and image[r][cc] == tcolor:
                st.append([r, cc])
                image[r][cc] = color
            
        return image
             
# @lc code=end

