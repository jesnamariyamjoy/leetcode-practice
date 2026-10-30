class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(n - 1):
            out = []
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                out.append(str(j - i))   # run length
                out.append(s[i])         # the repeated digit
                i = j
            s = "".join(out)
        return s