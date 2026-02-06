"""
 2. Add Two Numbers
 URL: https://leetcode.com/problems/add-two-numbers/
 Difficulty: Medium
 Topics: Linked List, Math, Recursion
 Date: 2026-02-06T06:31:36.183Z
"""

#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        curr=dummy
        carry = 0
        while l1 or l2 or carry:
            value=l1.val if l1 else 0
            value+=l2.val if l2 else 0
            value+=carry
            carry= value//10
            curr.next = ListNode(val=(value % 10))
            curr = curr.next
            if l1 :
                l1 = l1.next
            if l2 :
                l2 = l2.next

        return dummy.next
