"""
 98. Validate Binary Search Tree
 URL: https://leetcode.com/problems/validate-binary-search-tree/submissions/1926556458/
 Difficulty: Medium
 Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree
 Date: 2026-02-21T17:16:10.327Z
"""

#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node,low,high):
            if not node:
                return True

            if not (low<node.val<high):
                return False

            return (
                dfs(node.left,low,node.val) and dfs(node.right,node.val,high) 
            )
                 
        return dfs(root,float('-inf'),float('inf'))
#         self.val = val
#     def __init__(self, val=0, left=None, right=None):
# class TreeNode(object):
# Definition for a binary tree node.
