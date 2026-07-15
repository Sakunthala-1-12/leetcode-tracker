# Last updated: 7/15/2026, 3:17:40 PM
1class Solution:
2    def reverseKGroup(self, head, k):
3        dummy = ListNode(0)
4        dummy.next = head
5        groupPrev = dummy
6
7        while True:
8            kth = groupPrev
9            for _ in range(k):
10                kth = kth.next
11                if not kth:
12                    return dummy.next
13
14            groupNext = kth.next
15
16            prev = groupNext
17            curr = groupPrev.next
18
19            while curr != groupNext:
20                temp = curr.next
21                curr.next = prev
22                prev = curr
23                curr = temp
24
25            temp = groupPrev.next
26            groupPrev.next = kth
27            groupPrev = temp