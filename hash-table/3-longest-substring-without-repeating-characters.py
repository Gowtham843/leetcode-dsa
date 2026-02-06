"""
 3. Longest Substring Without Repeating Characters
 URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 Difficulty: Medium
 Topics: Hash Table, String, Sliding Window
 Date: 2026-02-06T16:26:59.415Z
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited=set()
        left=0
        max_length=0
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left+=1
            
            visited.add(s[right])
            max_length=max(max_length,right-left+1)
            
            
        return max_length
