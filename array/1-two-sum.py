"""
 1. Two Sum
 URL: https://leetcode.com/problems/two-sum/description/
 Difficulty: Easy
 Topics: Array, Hash Table
 Date: 2026-02-06T06:30:30.215Z
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=left+1
        while right<len(nums):
            if nums[left]+nums[right]==target:
                return [left,right]
            else:
                right+=1
                if right==len(nums):
                    left+=1
                    right=left+1
        return [-1,-1]
        
