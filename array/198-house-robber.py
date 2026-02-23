"""
 198. House Robber
 URL: https://leetcode.com/problems/house-robber/submissions/1928683048/
 Difficulty: Medium
 Topics: Array, Dynamic Programming
 Date: 2026-02-23T15:55:46.188Z
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1,num2=0,nums[0]
        for curr in nums[1:]:
            sum = max(num2,num1+curr)
            num1,num2=num2,sum
        
        return num2    
