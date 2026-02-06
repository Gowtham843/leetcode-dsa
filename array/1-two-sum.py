"""
 1. Two Sum
 URL: https://leetcode.com/problems/two-sum/
 Difficulty: Easy
 Topics: Array, Hash Table
 Date: 2026-02-06T06:27:42.486Z
"""

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
        :type target: int
        :type nums: List[int]
        """
    def twoSum(self, nums, target):
class Solution(object):
                    right=left+1
        return [-1,-1]
        
