"""
 10. Regular Expression Matching
 URL: https://leetcode.com/problems/regular-expression-matching/
 Difficulty: Hard
 Topics: String, Dynamic Programming, Recursion
 Date: 2026-02-15T18:08:20.576Z
"""

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
        m, n = len(s), len(p)
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
        
        return dp[m][n]
    def isMatch(self, s, p):
class Solution(object):
        
