# Last updated: 7/15/2026, 3:16:39 PM
1import heapq
2
3class Solution:
4    def mergeKLists(self, lists):
5        heap = []
6
7        for i, node in enumerate(lists):
8            if node:
9                heapq.heappush(heap, (node.val, i, node))
10
11        dummy = ListNode(0)
12        current = dummy
13
14        while heap:
15            val, i, node = heapq.heappop(heap)
16            current.next = node
17            current = current.next
18
19            if node.next:
20                heapq.heappush(heap, (node.next.val, i, node.next))
21
22        return dummy.next