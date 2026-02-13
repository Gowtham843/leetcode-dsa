"""
 66. Plus One
 URL: https://leetcode.com/problems/plus-one/submissions/1918251177/
 Difficulty: Easy
 Topics: Array, Math
 Date: 2026-02-13T17:30:52.716Z
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int("".join(str(x) for x in digits))+1
        return [int(d) for d in str(number)]
        
