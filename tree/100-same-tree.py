"""
 100. Same Tree
 URL: https://leetcode.com/problems/same-tree/submissions/1923492873/
 Difficulty: Easy
 Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
 Date: 2026-02-18T16:41:08.857Z
"""

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        # print(p.val,q.val)
        if p.val!=q.val:
            return False

        

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
