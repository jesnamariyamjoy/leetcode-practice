class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        cur_row = 0
        direction = -1  # will flip to +1 on first char

        for char in s:
            rows[cur_row] += char
            if cur_row == 0 or cur_row == numRows - 1:
                direction = -direction
            cur_row += direction

        return ''.join(rows)