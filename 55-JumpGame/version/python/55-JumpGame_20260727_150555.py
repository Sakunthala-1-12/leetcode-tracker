# Last updated: 7/27/2026, 3:05:55 PM
1class Solution:
2    def rotateRight(self, head, k):
3        if not head or not head.next or k == 0:
4            return head
5
6        length = 1
7        tail = head
8
9        while tail.next:
10            tail = tail.next
11            length += 1
12
13        k %= length
14        if k == 0:
15            return head
16
17        tail.next = head
18
19        steps = length - k
20        new_tail = tail
21
22        while steps:
23            new_tail = new_tail.next
24            steps -= 1
25
26        new_head = new_tail.next
27        new_tail.next = None
28
29        return new_head