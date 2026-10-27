from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        L = len(words[0])
        k = len(words)
        n = len(s)
        need = Counter(words)
        res = []

        for offset in range(L):
            left = offset
            count = 0
            window = Counter()

            for right in range(offset, n - L + 1, L):
                w = s[right:right + L]

                if w in need:
                    window[w] += 1
                    count += 1

                    # too many copies of w: shrink from the left
                    while window[w] > need[w]:
                        window[s[left:left + L]] -= 1
                        left += L
                        count -= 1

                    if count == k:
                        res.append(left)
                        # slide one word forward to keep searching
                        window[s[left:left + L]] -= 1
                        left += L
                        count -= 1
                else:
                    # invalid word: reset the window past it
                    window.clear()
                    count = 0
                    left = right + L

        return res