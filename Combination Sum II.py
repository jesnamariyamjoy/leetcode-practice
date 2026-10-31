class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    break  # sorted, so nothing later fits either
                if i > start and c == candidates[i - 1]:
                    continue  # skip duplicate at the same depth
                path.append(c)
                backtrack(i + 1, remaining - c)  # i + 1: each element used once
                path.pop()

        backtrack(0, target)
        return res