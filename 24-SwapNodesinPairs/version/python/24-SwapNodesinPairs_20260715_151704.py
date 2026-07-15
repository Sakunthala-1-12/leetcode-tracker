# Last updated: 7/15/2026, 3:17:04 PM
1class Solution:
2    def swapPairs(self, head):
3        dummy = ListNode(0)
4        dummy.next = head
5        prev = dummy
6
7        while prev.next and prev.next.next:
8            first = prev.next
9            second = first.next
10
11            first.next = second.next
12            second.next = first
13            prev.next = second
14
15            prev = first
16
17        return dummy.next