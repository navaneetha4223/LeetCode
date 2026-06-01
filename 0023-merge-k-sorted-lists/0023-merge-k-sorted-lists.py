# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for node in lists:
            while node:
                minHeap.append(node.val)
                node = node.next
        heapq.heapify(minHeap)

        head = current = ListNode(-1)
        while minHeap:
            current.next = ListNode(heapq.heappop(minHeap))
            current = current.next
        
        return head.next