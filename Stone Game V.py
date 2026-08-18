class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(10000)

        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        memo = {}

        def dp(i, j):
            if i == j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            best = 0
            for k in range(i, j):
                left = prefix[k + 1] - prefix[i]
                right = prefix[j + 1] - prefix[k + 1]
                if left <= right:
                    best = max(best, left + dp(i, k))
                if right <= left:
                    best = max(best, right + dp(k + 1, j))

            memo[(i, j)] = best
            return best

        return dp(0, n - 1)