# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle node of the linked list
        # Reverse the first half of the list step by step and compare with the second half of the list until the fast pointer meet its end
        
        slow = head
        fast = head

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            prev, curr = None, head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # Find the middle point:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half from slow
        reverse_head = reverseList(slow)
        while head and reverse_head:
            if head.val != reverse_head.val:
                return False
            head = head.next
            reverse_head = reverse_head.next
        return True