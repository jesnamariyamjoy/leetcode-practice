class Solution(object):
    def combinationSum(self, candidates, target):
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
                    break  # sorted, so nothing later can fit either
                path.append(c)
                backtrack(i, remaining - c)  # pass i, not i+1: reuse allowed
                path.pop()

        backtrack(0, target)
        return res