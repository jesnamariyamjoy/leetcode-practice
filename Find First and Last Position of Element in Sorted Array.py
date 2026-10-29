class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first_ge(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        left = first_ge(target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = first_ge(target + 1) - 1
        return [left, right]