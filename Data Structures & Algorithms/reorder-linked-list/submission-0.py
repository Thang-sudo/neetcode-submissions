# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2 -> 4 -> 6 -> 8 -> 10
        # 2 -> 4 -> 6
        # 10 -> 8
        # 2 -> 10 -> 4 -> 8 -> 6

        # Break the original linked list into 2 halves
        head1 = head
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        # Reverse the second linked list
        prev = None
        current = head2
        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        head2 = prev
        first, second = head1, head2
        # Merge head1 with head2
        while second is not None:
            print("first: " + str(first.val))
            print("second: " + str(second.val))
            firstNext = first.next
            secondNext = second.next

            first.next = second
            first = firstNext

            second.next = firstNext
            second = secondNext
            
        return None



        

        