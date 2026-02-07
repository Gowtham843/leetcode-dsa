"""
 5. Longest Palindromic Substring
 URL: https://leetcode.com/problems/longest-palindromic-substring/submissions/1911520415/
 Difficulty: Medium
 Topics: Two Pointers, String, Dynamic Programming
 Date: 2026-02-07T17:24:51.696Z
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        def expand(l,r):
            while (l>=0 and r<n and s[l]==s[r]):
                l-=1
                r+=1
                
            return s[l+1:r]
        
        longest=''
        for i in range(n):
            odd=expand(i,i)
            if(len(odd)>len(longest)):
                longest=odd    
            even=expand(i,i+1)
            if(len(even)>len(longest)):
