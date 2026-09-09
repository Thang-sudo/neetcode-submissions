# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1, curr2 = l1, l2
        prev = ListNode(0, None)
        result = ListNode(0, None)
        prev.next = result

        dummy = result 
        
        while curr1 or curr2:
            l1Val = 0 if curr1 is None else curr1.val
            l2Val = 0 if curr2 is None else curr2.val
            nodeSum = l1Val + l2Val + carry
            if nodeSum >= 10:
                nodeSum = nodeSum - 10
                carry = 1
            else:
                carry = 0
            prev = result
            result = ListNode(nodeSum, None)
            prev.next = result

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        if carry > 0:
            prev = result
            result = ListNode(carry, None)
            prev.next = result

        return dummy.next


            
        
        