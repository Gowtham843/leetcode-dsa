"""
 62. Unique Paths
 URL: https://leetcode.com/problems/unique-paths/
 Difficulty: Medium
 Topics: Math, Dynamic Programming, Combinatorics
 Date: 2026-02-20T17:09:15.436Z
"""

class Solution(object):
    def uniquePaths(self, m, n):
        dp = [1]*n
        for _ in range(1,m):
            for j in range(1,n):
                dp[j]+=dp[j-1]
        
        return dp[-1]
        
