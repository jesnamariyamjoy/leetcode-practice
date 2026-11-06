class Solution(object):
    def canJump(self, nums):
        """:type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        n = len(nums)
        
        for i in range(n):
            # If our current position is beyond the maximum reach, we're stuck
            if i > max_reach:
                return False
            
            # Update the furthest index we can reach
            max_reach = max(max_reach, i + nums[i])
            
            # If we can already reach or surpass the last index, return True early
            if max_reach >= n - 1:
                return True
                
        return True