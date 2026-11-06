class Solution(object):
    def spiralOrder(self, matrix):
        """:type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse from left to right along the top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            
            # 2. Traverse from top to bottom along the right column
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1
            
            # 3. Traverse from right to left along the bottom row (if rows remain)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
                
            # 4. Traverse from bottom to top along the left column (if columns remain)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
                
        return res