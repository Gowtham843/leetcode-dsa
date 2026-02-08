"""
 14. Longest Common Prefix
 URL: https://leetcode.com/problems/longest-common-prefix/submissions/1912476572/
 Difficulty: Easy
 Topics: Array, String, Trie
 Date: 2026-02-08T13:50:48.548Z
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix=strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix=prefix[:-1]
                if prefix=="":
                    return ""
            
        return prefix



