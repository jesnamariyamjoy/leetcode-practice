class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = -1
        match = 0
        
        while s_idx < s_len:
            # If the current characters match or pattern has '?'
            if p_idx < p_len and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            # If pattern has '*', record the star position and current string match index
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                match = s_idx
                p_idx += 1
            # If there is a previous '*', backtrack and let it match one more character
            elif star_idx != -1:
                p_idx = star_idx + 1
                match += 1
                s_idx = match
            else:
                return False
                
        # Check for remaining characters in pattern (must all be '*')
        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == p_len