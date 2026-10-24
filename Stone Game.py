class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        pre = [0] * (n + 1)
        for i, v in enumerate(stoneValue):
            pre[i + 1] = pre[i] + v

        # dp[l][r] = best score for the row stoneValue[l..r]
        dp = [[0] * n for _ in range(n)]
        # PL[l][r] = max over j in [l, r] of sum(l..j) + dp[l][j]   (keep a prefix)
        # PR[r][s] = max over t in [s, r] of sum(t..r) + dp[t][r]   (keep a suffix)
        PL = [[0] * n for _ in range(n)]
        PR = [[0] * n for _ in range(n)]
        for i in range(n):
            PL[i][i] = stoneValue[i]
            PR[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                total = pre[r + 1] - pre[l]

                # first split point m where left sum >= right sum
                lo, hi = l, r - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if 2 * (pre[mid + 1] - pre[l]) >= total:
                        hi = mid
                    else:
                        lo = mid + 1
                m = lo
                sl = pre[m + 1] - pre[l]

                if 2 * sl < total:
                    # every split has left < right: Alice keeps the left row
                    best = PL[l][m]
                else:
                    # splits before m: left < right, keep left
                    best = PL[l][m - 1] if m > l else 0
                    if 2 * sl == total:
                        # tie: Alice may keep either side
                        best = max(best,
                                   sl + dp[l][m],
                                   total - sl + dp[m + 1][r])
                        s = m + 2
                    else:
                        s = m + 1
                    # splits after m: left > right, keep right
                    if s <= r:
                        best = max(best, PR[r][s])

                dp[l][r] = best
                val = total + best
                PL[l][r] = max(PL[l][r - 1], val)
                PR[r][l] = max(PR[r][l + 1], val)

        return dp[0][n - 1]