class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        n = len(nums)
        count = defaultdict(int)

        for i in range(n - k + 1):
            window = set(nums[i:i + k])   # dedupe within a window so repeats inside one window don't double count
            for v in window:
                count[v] += 1

        candidates = [v for v, c in count.items() if c == 1]
        return max(candidates) if candidates else -1