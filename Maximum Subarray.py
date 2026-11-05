class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Either extend the previous subarray or start a new one from the current element
            current_sum = max(nums[i], current_sum + nums[i])
            # Update the global maximum if the current subarray sum is greater
            max_sum = max(max_sum, current_sum)
            
        return max_sum