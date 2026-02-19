"""
 206. Reverse Linked List
 URL: https://leetcode.com/problems/reverse-linked-list/
 Difficulty: Easy
 Topics: Linked List, Recursion
 Date: 2026-02-19T17:21:24.566Z
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        curr = head
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr=nxt
            
        return prev
        
