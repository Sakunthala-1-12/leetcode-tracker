# Last updated: 7/27/2026, 3:19:53 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def deleteDuplicates(self, head):
8        current = head
9
10        while current and current.next:
11            if current.val == current.next.val:
12                current.next = current.next.next
13            else:
14                current = current.next
15
16        return head
17        