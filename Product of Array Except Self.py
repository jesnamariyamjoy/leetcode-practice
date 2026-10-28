class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        # Pass 1: answer[i] = product of all elements to the left of i
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # Pass 2: multiply by the product of all elements to the right of i
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer