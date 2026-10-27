class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = []
        for i in range(m):
            if i == 0:
                grid.append('.' * n)              # whole top row is free
            else:
                grid.append('#' * (n - 1) + '.')  # only last column is free
        return grid