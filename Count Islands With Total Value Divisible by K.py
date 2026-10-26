class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    total = 0
                    stack = [(i, j)]
                    visited[i][j] = True

                    while stack:
                        r, c = stack.pop()
                        total += grid[r][c]

                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = r + dr, c + dc
                            if (0 <= nr < m and 0 <= nc < n
                                    and grid[nr][nc] > 0
                                    and not visited[nr][nc]):
                                visited[nr][nc] = True
                                stack.append((nr, nc))

                    if total % k == 0:
                        count += 1

        return count