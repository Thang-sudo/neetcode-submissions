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

        current = head
        length = 0
        while current:
            current = current.next
            length += 1
        removeIndex = length - n
        i = 0
        prev = None
        current = head
        print(length)
        print("removeIndex: " + str(removeIndex))
        while i < removeIndex:
            prev = current
            current = current.next
            i += 1
        if prev:
            prev.next = current.next
            current.next = None
        else:
            head = head.next
        return head
            
            
