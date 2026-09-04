# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # scan the list to get number of nodes
        # remove the node at length - n
        # how to remove a node. A prev pointer and current pointer.
        # prev.next = current.next
        # current.next = None

        # current = head
        # length = 0
        # while current:
        #     current = current.next
        #     length += 1
        # removeIndex = length - n
        # i = 0
        # prev = None
        # current = head
        
        # while i < removeIndex:
        #     prev = current
        #     current = current.next
        #     i += 1
        # if prev:
        #     prev.next = current.next
        #     current.next = None
        # else:
        #     head = head.next
        # return head

        # Dummy node handles the case where the head must be removed
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Move right n nodes ahead of left
        for _ in range(n):
            right = right.next

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # left.next is the nth node from the end
        left.next = left.next.next

        return dummy.next


            
            
