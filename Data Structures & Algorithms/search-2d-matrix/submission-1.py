class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            m = (top + bot) // 2
            if target < matrix[m][0]:
                bot -= 1
            elif target > matrix[m][-1]:
                top += 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, len(matrix[0]) - 1
        row = (top + bot) // 2
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l += 1
            elif target < matrix[row][m]:
                r -= 1
            else:
                return True
        return False
        