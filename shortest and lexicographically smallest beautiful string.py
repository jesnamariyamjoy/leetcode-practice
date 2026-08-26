class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ones = [i for i, c in enumerate(s) if c == '1']
        if len(ones) < k:
            return ""
        
        best = None
        min_len = float('inf')
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            length = end - start + 1
            candidate = s[start:end + 1]
            
            if length < min_len:
                min_len = length
                best = candidate
            elif length == min_len and candidate < best:
                best = candidate
        
        return best