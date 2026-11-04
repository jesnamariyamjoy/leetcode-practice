from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a unique canonical key for its anagram group
            key = "".join(sorted(s))
            anagram_map[key].append(s)
            
        return list(anagram_map.values())