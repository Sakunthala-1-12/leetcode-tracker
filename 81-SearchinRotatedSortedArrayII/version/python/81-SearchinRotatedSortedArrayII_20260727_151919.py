# Last updated: 7/27/2026, 3:19:19 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def deleteDuplicates(self, head):
8        dummy = ListNode(0)
9        dummy.next = head
10        prev = dummy
11
12        while head:
13            if head.next and head.val == head.next.val:
14                while head.next and head.val == head.next.val:
15                    head = head.next
16                prev.next = head.next
17            else:
18                prev = prev.next
19
20            head = head.next
21
22        return dummy.next