# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # The point of this is to flip the arrow in linked list meaning the current node must point to the previous node
        # current node starts from head, so its previous must be None
        prev = None
        current = head
        while current != None:
            # save the next node, so we can move current node
            next_node = current.next
            # revert the arrow
            current.next = prev
            prev = current
            current = next_node
        return prev
