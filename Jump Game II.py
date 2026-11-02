class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We only need to iterate up to the second to last element
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of the current jump range, make a jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps