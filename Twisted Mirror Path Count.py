class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # R[i][j]: ways of attempting to enter (i, j) while moving right
        # D[i][j]: ways of attempting to enter (i, j) while moving down
        R = [[0] * n for _ in range(m)]
        D = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    r, d = 1, 0
                    # start cell is empty, so treat it as a non-mirror landing
                    total = 1
                else:
                    r, d = R[i][j], D[i][j]
                    total = (r + d) % MOD

                if i == m - 1 and j == n - 1:
                    return total

                if grid[i][j] == 0:
                    # robot rests here; it may go right or down
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + total) % MOD
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + total) % MOD
                else:
                    # mirror: entered moving right -> pushed down,
                    #         entered moving down  -> pushed right
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + r) % MOD
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + d) % MOD

        return 0