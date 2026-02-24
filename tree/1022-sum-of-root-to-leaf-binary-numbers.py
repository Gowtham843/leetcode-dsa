"""
 1022. Sum of Root To Leaf Binary Numbers
 URL: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/?envType=daily-question&envId=2026-02-24
 Difficulty: Easy
 Topics: Tree, Depth-First Search, Binary Tree
 Date: 2026-02-24T17:08:19.123Z
"""

    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, curr):
            if not node:
                return 0
            
            curr=(curr << 1)|node.val

            if not node.left and not node.right:
                return curr

#         self.right = right
class Solution(object):
#         self.val = val
#         self.left = left
#     def __init__(self, val=0, left=None, right=None):
# class TreeNode(object):
            return dfs(node.left,curr)+dfs(node.right,curr)
        
        return dfs(root,0)
# Definition for a binary tree node.
