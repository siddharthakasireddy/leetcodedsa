# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        # Min-heap to store (node value, index, node reference)
        heap = []
        
        # Push first node of every list into heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        # Dummy head for final result
        dummy = ListNode()
        curr = dummy
        
        # Extract smallest node from heap and push its next
        while heap:
            val, idx, node = heapq.heappop(heap)
            
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next

        