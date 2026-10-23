class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pairs:
                # Closing bracket: top of stack must be its matching opener
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                # Opening bracket: remember it
                stack.append(ch)

        # Valid only if every opener was matched
        return not stack