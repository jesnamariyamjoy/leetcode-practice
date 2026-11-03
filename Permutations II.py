class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        visited = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                # If this element is visited, skip it
                if visited[i]:
                    continue
                # If this element is a duplicate of the previous one and the previous
                # one hasn't been used yet, skip it to avoid duplicate permutations
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                visited[i] = False
                
        backtrack([])
        return res