"""
 1. Two Sum
 URL: https://leetcode.com/problems/two-sum/
 Difficulty: Easy
 Topics: Array, Hash Table
 Date: 2026-02-15T18:12:48.262Z
"""

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], index]
            hashmap[num] = index
        return [-1, -1]

        
