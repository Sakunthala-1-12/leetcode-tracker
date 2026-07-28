# Last updated: 7/28/2026, 3:04:26 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def partition(self, head, x):
8        before = ListNode(0)
9        after = ListNode(0)
10
11        before_curr = before
12        after_curr = after
13
14        while head:
15            if head.val < x:
16                before_curr.next = head
17                before_curr = before_curr.next
18            else:
19                after_curr.next = head
20                after_curr = after_curr.next
21            head = head.next
22
23        after_curr.next = None
24        before_curr.next = after.next
25
26        return before.next
27        