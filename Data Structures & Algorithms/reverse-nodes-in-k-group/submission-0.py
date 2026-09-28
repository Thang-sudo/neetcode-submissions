# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKthNode(self, start: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not start:
            return None
        curr = start
        count = 1
        while count < k and curr:
            curr = curr.next
            count += 1
        return None if count < k else curr
    
    def reverseLinkedList(self, start: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
        # Reverses nodes from `start` through `end` (INCLUSIVE).
        # Returns the new head of the reversed segment (== end before reversal).
        # i.e 1 -> 2 -> 3. It should return 3
        tail_next = end.next # what the tail is pointing to. Need to connect the original head with this tail_next
        prev, curr = tail_next, start
        while curr != tail_next:
            tmp = curr.next # save the next node to process
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prevTail = dummy
        curr = head
        while curr:
            kthNode = self.getKthNode(curr, k)
            if not kthNode:
                break
            nextGroupNode = kthNode.next
            headReversed = self.reverseLinkedList(curr, kthNode) 
            prevTail.next = headReversed
            prevTail = curr
            curr = nextGroupNode
        return dummy.next

        



        